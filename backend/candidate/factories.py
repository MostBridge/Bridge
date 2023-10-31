import factory

from django.utils import timezone
from django.contrib.auth import get_user_model
from factory.django import DjangoModelFactory
from faker.providers import BaseProvider
from factory.fuzzy import FuzzyInteger

from candidate.models import (
    Profession,
    Technology,
    Contact,
    Candidate,
    Town,
    Employment,
    Favorite,
    View,
)

User = get_user_model()
LOW_LIMIT = 0
HIGH_LIMIT = 50


class Provider(BaseProvider):
    """Provider для создания данных."""

    tech_types = ["Django", "Html", "Css", "Docker", "JS"]

    town_types = [
        "Moscow",
        "Saint-Petersburg",
    ]

    work_format_types = ["Удалёнка", "Офис", "Гибрид"]

    experiences = ["Нет опыта", "1 - 3 года", "3 - 6 лет"]

    grade_types = ["junior", "middle"]

    profession_types = [
        "Backend-разработчик",
        "Frontend-разработчик",
        "Дизайнер",
    ]

    def tech_type(self):
        """Типы технологий."""
        return self.random_element(self.tech_types)

    def town_type(self):
        """Типы городов."""
        return self.random_element(self.town_types)

    def work_format_type(self):
        """Типы рабочих форматов."""
        return self.random_element(self.work_format_types)

    def grades_types(self):
        """Типы грейда."""
        return self.random_element(self.grade_types)

    def experience(self):
        """Опыт работы."""
        return self.random_element(self.experiences)

    def professions_types(self):
        """Типы профессий."""
        return self.random_element(self.profession_types)


factory.Faker.add_provider(Provider)


class ProfessionFactory(DjangoModelFactory):
    """Фабрика профессий для тестирования проекта."""

    class Meta:
        model = Profession
        django_get_or_create = ("name",)

    name = factory.Faker("professions_types")
    slug = factory.Faker("slug")


class TechnologyFactory(DjangoModelFactory):
    """Фабрика технологий для тестирования проекта."""

    class Meta:
        model = Technology
        django_get_or_create = ("name",)

    name = factory.Faker("tech_type")
    slug = factory.Faker("slug")


class EmploymentFactory(DjangoModelFactory):
    """Фабрика технологий для тестирования проекта."""

    class Meta:
        model = Employment
        django_get_or_create = ("name",)

    name = factory.Faker("work_format_type")
    slug = factory.Faker("slug")


class TownFactory(DjangoModelFactory):
    """Фабрика городов для тестирования проекта."""

    class Meta:
        model = Town
        django_get_or_create = ("id",)

    id = FuzzyInteger(1, 1111)


class CandidateFactory(DjangoModelFactory):
    """Фабрика кандидатов для тестирования проекта."""

    class Meta:
        model = Candidate

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    employment = factory.RelatedFactoryList(EmploymentFactory)
    project = FuzzyInteger(LOW_LIMIT, HIGH_LIMIT)
    portfolio = factory.Faker("url")
    reviews = factory.Faker("url")
    profession = factory.SubFactory(ProfessionFactory)
    experience = factory.Faker("experience")
    technology = factory.RelatedFactoryList(TechnologyFactory)
    grade = factory.Faker("grades_types")
    town = factory.SubFactory(TownFactory)
    created_date = timezone.now()


class ContactFactory(DjangoModelFactory):
    """Фабрика контактов для тестирования проекта."""

    class Meta:
        model = Contact

    candidate = factory.SubFactory(CandidateFactory)
    phone_number = factory.Faker("phone_number", locale="ru_RU")
    email = factory.Faker("email")
    telegram = factory.Faker("user_name")


class UserFactory(DjangoModelFactory):
    """Фабрика контактов для тестирования проекта."""

    class Meta:
        model = User
        django_get_or_create = ("username",)

    email = factory.Faker("email")
    username = factory.Faker("user_name")
    password = factory.django.Password("pw")


class ViewFactory(DjangoModelFactory):
    """Фабрика контактов для тестирования проекта."""

    class Meta:
        model = View

    candidate = factory.SubFactory(CandidateFactory)
    user = factory.SubFactory(UserFactory)


class FavoriteFactory(DjangoModelFactory):
    """Фабрика избранного для тестирования проекта."""

    class Meta:
        model = Favorite

    candidate = factory.SubFactory(CandidateFactory)


def create_profession(amount: int = 1):
    """Создание профессий для тестов программы."""
    ProfessionFactory.create_batch(amount)


def create_technology(amount: int = 1):
    """Создание технологии для тестов программы."""
    TechnologyFactory.create_batch(amount)


def create_contacts(amount: int = 1):
    """Создание контактов для тестов программы."""
    ContactFactory.create_batch(amount)


def create_favorites(amount: int = 1):
    """Создание профессий для тестов программы."""
    FavoriteFactory.create_batch(amount)
