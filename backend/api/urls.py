from django.urls import include, path

from api.v1 import urls as v1_urls

app_name = "api"

urlpatterns = [path("v1/", include(v1_urls))]
