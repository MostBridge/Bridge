from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class BaseCaseForCandidateTests(APITestCase):
    USERNAME = "auth_user"
    EMAIL = "auth_user@example.com"
    PASSWORD = "password"

    ENDPOINTS = (
        reverse("api:v1:employment-list"),
        reverse("api:v1:technology-list"),
        reverse("api:v1:town-list"),
        reverse("api:v1:profession-list"),
        reverse("api:v1:candidates-list"),
    )

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.auth_client = APIClient()
        user = User.objects.create_user(
            email=cls.EMAIL,
            username=cls.USERNAME,
            password=cls.PASSWORD,
        )
        refresh = RefreshToken.for_user(user=user)
        cls.auth_client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}"
        )
