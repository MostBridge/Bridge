from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.v1.views import (
    CandidateViewSet,
    MyUsersViewSet,
    ProfessionViewSet,
    TechnologyViewSet,
    TownViewSet,
)

app_name = "api"

router_v1 = DefaultRouter()

router_v1.register("technology", TechnologyViewSet, basename="technology")
router_v1.register("town", TownViewSet, basename="town")
router_v1.register("profession", ProfessionViewSet, basename="profession")
router_v1.register("candidates", CandidateViewSet, basename="candidates")
router_v1.register("users", MyUsersViewSet, basename="users")


urlpatterns = [
    path("", include(router_v1.urls)),
    path("", include("djoser.urls.base")),
    path("auth/", include("djoser.urls.jwt")),
]
