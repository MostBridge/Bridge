from django.test import TestCase
from candidate.models import (
    Profession,
    Town,
    Technology,
    Employment,
    Candidate,
)

from candidate.factories import (
    ProfessionFactory,
    TownFactory,
    TechnologyFactory,
    EmploymentFactory,
    CandidateFactory,
)


class CandidateModelTests(TestCase):
    """
    Test class for candidate models
    """

    def test_creating_profession(self):
        """
        Test creating profession model object
        """
        profession = ProfessionFactory.create()
        model_post = Profession.objects.get(name=profession)

        self.assertEqual(profession.name, model_post.name)

    def test_creating_town(self):
        """
        Test creating town model object
        """
        town = TownFactory.create()
        model_post = Town.objects.get(city=town)

        self.assertEqual(town.city, model_post.city)

    def test_creating_technology(self):
        """
        Test creating technology model object
        """
        technology = TechnologyFactory.create()
        model_post = Technology.objects.get(name=technology)

        self.assertEqual(technology.name, model_post.name)
        self.assertEqual(technology.slug, model_post.slug)

    def test_creating_employment(self):
        """
        Test creating employment model object
        """
        employment = EmploymentFactory.create()
        model_post = Employment.objects.get(name=employment)
        self.assertEqual(employment.name, model_post.name)
        self.assertEqual(employment.slug, model_post.slug)

    def test_creating_candidate(self):
        """
        Test creating candidate model object
        """
        candidate = CandidateFactory.create()
        model_post = Candidate.objects.get(id=candidate.id)
        self.assertEqual(candidate.employment, model_post.employment)
        self.assertEqual(candidate.profession, model_post.profession)
        self.assertEqual(candidate.grade, model_post.grade)
        self.assertEqual(candidate.town, model_post.town)
        self.assertEqual(candidate.created_date, model_post.created_date)
