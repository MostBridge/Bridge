from djoser.views import UserViewSet

from api.v1.serializers import (
    ProfessionSerializer,
    TechnologySerializer,
    TownSerializer,
)
from api.v1.mixins import ListViewSet
from candidate.models import Profession, Technology, Town


class MyUsersViewSet(UserViewSet):
    """Вьюсет пользователя."""


class TechnologyViewSet(ListViewSet):
    """Вьюсет пользователя."""

    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer


class TownViewSet(ListViewSet):
    """Вьюсет города."""

    queryset = Town.objects.all()
    serializer_class = TownSerializer


class ProfessionViewSet(ListViewSet):
    """Вьюсет професии."""

    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer
