import requests
from django.shortcuts import get_object_or_404
from djoser.views import UserViewSet
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from api.v1.serializers import (
    CandidateSerializer,
    CandidateShortSerializer,
    EmploymentSerializer,
    FavoriteSerializer,
    ProfessionSerializer,
    TechnologySerializer,
    TownSerializer,
)
from candidate.models import (
    Candidate,
    Employment,
    Favorite,
    Profession,
    Technology,
    Town,
)


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

    @action(
        detail=True,
        serializer_class=None,
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


class EmploymentViewSet(viewsets.ReadOnlyModelViewSet):
    """Класс формата работы."""

    queryset = Employment.objects.all()
    serializer_class = EmploymentSerializer
