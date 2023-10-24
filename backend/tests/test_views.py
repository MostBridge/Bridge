from django.test import TestCase
from http import HTTPStatus

from candidate.factories import CandidateFactory

ENDPOINTS = ("technology", "candidates", "town", "profession", "employment")


class CandidateViewTests(TestCase):
    """
    Test class for candidate Views
    """

    def test_check_view(self):
        """
        Test check view
        """
        for endpoint in ENDPOINTS:
            response = self.client.get(f"/api/v1/{endpoint}/")
            self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_check_registration_view(self):
        """
        Test for check registration
        """
        response = self.client.post(
            "/api/v1/users/",
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
        response = self.client.get(f"/api/v1/town/{candidate.town.id}/")
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_profession_id_view(self):
        """
        Test profession id view
        """
        candidate = CandidateFactory.create()
        response = self.client.get(
            f"/api/v1/profession/{candidate.profession.id}/"
        )
        self.assertEqual(response.status_code, HTTPStatus.OK)
