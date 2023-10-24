from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from candidate.models import (
    Candidate,
    Contact,
    Employment,
    Profession,
    Technology,
    Town,
)


class EmploymentSerializer(serializers.ModelSerializer):
    """Сериализатор формата работы."""

    class Meta:
        model = Employment
        fields = (
            "id",
            "name",
            "slug",
        )
        read_only_fields = (
            "id",
            "name",
            "slug",
        )


class TechnologySerializer(serializers.ModelSerializer):
    """Сериализация для технологий."""

    class Meta:
        model = Technology
        fields = ("id", "name", "slug")
        read_only_fields = ("name", "slug")


class TownSerializer(serializers.ModelSerializer):
    """Сериализатор города."""

    class Meta:
        model = Town
        fields = (
            "id",
            "region",
            "city",
            "district",
        )
        read_only_fields = (
            "id",
            "region",
            "city",
            "district",
        )


class ProfessionSerializer(serializers.ModelSerializer):
    """Сериализация для профессии."""

    class Meta:
        model = Profession
        fields = ("id", "name")
        read_only_fields = ("name",)


class ContactSerializer(serializers.ModelSerializer):
    """Сериализатор контактов."""

    class Meta:
        model = Contact
        fields = (
            "id",
            "phone_number",
            "email",
            "telegram",
        )
        read_only_fields = (
            "id",
            "phone_number",
            "email",
            "telegram",
        )


class CandidateSerializer(serializers.ModelSerializer):
    """Сериализатор кандидатов."""

    contacts = ContactSerializer()
    town = TownSerializer()
    profession = ProfessionSerializer()
    employment = EmploymentSerializer(many=True)
    photo = Base64ImageField()

    class Meta:
        model = Candidate
        fields = (
            "id",
            "contacts",
            "town",
            "profession",
            "grade",
            "employment",
            "photo",
        )
        read_only_fields = (
            "id",
            "contacts",
            "town",
            "profession",
            "grade",
            "employment",
            "photo",
        )
