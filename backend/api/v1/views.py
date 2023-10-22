from djoser.views import UserViewSet
from rest_framework import viewsets

from api.v1.serializers import (
    ProfessionSerializer,
    TechnologySerializer,
    TownSerializer,
)
from candidate.models import Profession, Technology, Town


class MyUsersViewSet(UserViewSet):
    """Вьюсет пользователя."""


class TechnologyViewSet(viewsets.ModelViewSet):
    """Вьюсет пользователя."""

    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer


class TownViewSet(viewsets.ModelViewSet):
    """Вьюсет города."""

    queryset = Town.objects.all()
    serializer_class = TownSerializer


class ProfessionViewSet(viewsets.ModelViewSet):
    """Вьюсет професии."""

    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer
