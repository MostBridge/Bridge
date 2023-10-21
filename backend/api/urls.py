from django.urls import include, path
from rest_framework.routers import DefaultRouter

from backend.api.views import MyUsersViewSet

app_name = "api"

router = DefaultRouter()

router.register(r"users", MyUsersViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

]