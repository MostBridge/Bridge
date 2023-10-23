from random import choice

import factory
from factory.django import DjangoModelFactory
from faker.providers import BaseProvider

from candidate.models import Profession, Technology, Contact, Candidate, Town


class Provider(BaseProvider):
    """Provider для создания данных."""

    tech_types = [
        "Django",
        "Html",
        "Css",
        "Docker",
    ]

    town_types = [
        "Moscow",
        "Saint-Petersburg",
    ]

    def tech_type(self):
        """Типы технологий."""
        return self.random_element(self.tech_types)

    def town_type(self):
        """Типы городов."""
        return self.random_element(self.town_types)


factory.Faker.add_provider(Provider)


class ProfessionFactory(DjangoModelFactory):
    """Фабрика профессий для тестирования проекта."""

    class Meta:
        model = Profession

    name = factory.Faker("job")


class TechnologyFactory(DjangoModelFactory):
    """Фабрика технологий для тестирования проекта."""

    class Meta:
        model = Technology
        django_get_or_create = ("name",)

    name = factory.Faker("tech_type")
    slug = factory.Faker("slug")


class TownFactory(DjangoModelFactory):
    """Фабрика городов для тестирования проекта."""

    class Meta:
        model = Town
        django_get_or_create = ("city",)

    city = factory.Faker("town_type")


class CandidateFactory(DjangoModelFactory):
    """Фабрика кандидатов для тестирования проекта."""

    class Meta:
        model = Candidate

    profession = factory.SubFactory(ProfessionFactory)
    grade = choice(["Junior", "MIDLE"])
    town = factory.SubFactory(TownFactory)


class ContactFactory(DjangoModelFactory):
    """Фабрика контактов для тестирования проекта."""

    class Meta:
        model = Contact

    candidate = factory.SubFactory(CandidateFactory)
    phone_number = factory.Faker("phone_number")
    email = factory.Faker("email")
    telegram = factory.Faker("user_name")


def create_profession(amount: int = 1):
    """Создание профессий для тестов программы."""
    ProfessionFactory.create_batch(amount)


def create_contacts(amount: int = 1):
    """Создание контактов для тестов программы."""
    ContactFactory.create_batch(amount)
