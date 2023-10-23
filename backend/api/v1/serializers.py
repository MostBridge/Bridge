from rest_framework import serializers

from candidate.models import Candidate, Contact, Profession, Technology, Town


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

    class Meta:
        model = Candidate
        fields = (
            "id",
            "contacts",
            "town",
            "profession",
            "grade",
        )
        read_only_fields = (
            "id",
            "contacts",
            "town",
            "profession",
            "grade",
        )
