from djoser.views import UserViewSet
from rest_framework import viewsets

from api.v1.serializers import (
    CandidateSerializer,
    ProfessionSerializer,
    TechnologySerializer,
    TownSerializer,
)
from candidate.models import Candidate, Profession, Technology, Town


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
