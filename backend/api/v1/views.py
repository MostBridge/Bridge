import requests
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from djoser.views import UserViewSet
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend

from api.v1.serializers import (
    CandidateSerializer,
    CandidateShortSerializer,
    EmploymentSerializer,
    FavoriteDownloadSerializers,
    FavoriteSerializer,
    ProfessionSerializer,
    TechnologySerializer,
    TownSerializer,
    VacancySerializer,
    VacancySerializerCreate,
)
from api.v1.filters import CandidateFilter
from candidate.models import (
    Candidate,
    Employment,
    Favorite,
    Profession,
    Technology,
    Town,
    View,
)
from candidate.utils.download import download_files
from vacancy.models import Vacancy

User = get_user_model()


class UserActivationView(APIView):
    """Обработка данных для активации юзера."""

    @staticmethod
    def get(request, uid, token):
        """Формирование POST-запроса активации юзера."""
        protocol = "https://" if request.is_secure() else "http://"
        post_url = f"{protocol}{request.get_host()}/api/v1/users/activation/"
        post_data = {"uid": uid, "token": token}
        result = requests.post(post_url, data=post_data)
        content = result.text
        return Response(content)


class MyUsersViewSet(UserViewSet):
    """Вьюсет пользователя."""


class TechnologyViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет пользователя."""

    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer


class TownViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет городов России по регионам."""

    queryset = Town.objects.all()
    serializer_class = TownSerializer


class ProfessionViewSet(viewsets.ReadOnlyModelViewSet):
    """Вьюсет професии."""

    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer


class CandidateViewSet(viewsets.ReadOnlyModelViewSet):
    """Класс кандидатов."""

    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CandidateFilter

    def retrieve(self, request, *args, **kwargs):
        """Добавление записи в таблицу просмотренных кандидатов."""
        current_user = self.request.user
        candidate = self.get_object()
        if not current_user.viewed.filter(candidate=candidate).exists():
            View.objects.create(candidate=candidate, user=self.request.user)
        serializer = CandidateSerializer(
            candidate, context={"request": request}
        )
        return Response(serializer.data)

    @action(
        detail=True,
        methods=(
            "POST",
            "DELETE",
        ),
    )
    def favorite(self, request, pk=None):
        """Добавление/удаление кандидатов в избранное."""
        candidate = get_object_or_404(Candidate, pk=pk)
        current_user = self.request.user
        serializer = FavoriteSerializer(
            data={"candidate": pk, "user": current_user.id},
            context={"method": self.request.method},
        )
        serializer.is_valid(raise_exception=True)
        if self.request.method == "POST":
            Favorite.objects.create(
                candidate=candidate, user=self.request.user
            )
            serializer = CandidateShortSerializer(candidate)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        elif self.request.method == "DELETE":
            favorite = candidate.favorite.filter(user=self.request.user)
            favorite.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=("GET",))
    def resumes_download(self, request):
        """Скачивание резюме избранных кандидатов."""
        current_user = self.request.user
        serializer = FavoriteDownloadSerializers(
            data={"user": current_user.id}
        )
        serializer.is_valid(raise_exception=True)
        return download_files(serializer.validated_data)


class EmploymentViewSet(viewsets.ReadOnlyModelViewSet):
    """Класс формата работы."""

    queryset = Employment.objects.all()
    serializer_class = EmploymentSerializer


class VacancyViewSet(viewsets.ModelViewSet):
    """Класс вакансий."""

    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer

    def perform_create(self, serializer):
        """При создании вакансии author текущий user."""
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        """При обновлении вакансии author текущий user."""
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        """Метод изменения класса сериализатора при разных методах."""
        if self.request.method in ("POST", "PATCH"):
            return VacancySerializerCreate
        return VacancySerializer

    def create(self, request, *args, **kwargs):
        """Переопределение сериализатора выходных данных при создании."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        response_serializer = VacancySerializer(instance=serializer.instance)
        headers = self.get_success_headers(serializer.data)
        return Response(
            response_serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers,
        )

    def update(self, request, *args, **kwargs):
        """Переопределение сериализатора выходных данных при обновлении."""
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial
        )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, "_prefetched_objects_cache", None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        response_serializer = VacancySerializer(instance=serializer.instance)
        return Response(response_serializer.data)
