from http import HTTPStatus

from django.urls import reverse

from candidate.factories import CandidateFactory
from tests.fixtures import BaseCaseForCandidateTests


class CandidateViewTests(BaseCaseForCandidateTests):
    """
    Test class for candidate Views
    """

    def test_check_view(self):
        """
        Test check view
        """
        for endpoint in self.ENDPOINTS:
            with self.subTest(endpoint=endpoint):
                response = self.client.get(endpoint)
                self.assertEqual(response.status_code, HTTPStatus.UNAUTHORIZED)

        for endpoint in self.ENDPOINTS:
            with self.subTest(endpoint=endpoint):
                response = self.auth_client.get(endpoint)
                self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_check_registration_view(self):
        """
        Test for check registration
        """
        response = self.client.post(
            reverse("api:v1:users-list"),
            {
                "email": "user@example.com",
                "username": "user",
                "password": "sfafs23efdssa",
            },
        )
        self.assertEqual(response.status_code, HTTPStatus.CREATED)

    def test_town_id_view(self):
        """
        Test town id view
        """
        candidate = CandidateFactory.create()
        response = self.auth_client.get(
            reverse("api:v1:town-detail", kwargs={"pk": candidate.town.id})
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_profession_id_view(self):
        """
        Test profession id view
        """
        candidate = CandidateFactory.create()
        response = self.auth_client.get(
            reverse(
                "api:v1:profession-detail",
                kwargs={"pk": candidate.profession.id},
            )
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)
