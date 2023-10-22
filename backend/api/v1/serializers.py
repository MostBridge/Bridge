from rest_framework import serializers

from candidate.models import Candidate, Profession, Technology, Town


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


class CandidateSerializer(serializers.ModelSerializer):
    """Сериализатор кандидатов."""

    class Meta:
        model = Candidate
        fields = (
            "id",
            "contacts",
            "town",
        )
        read_only_fields = (
            "id",
            "contacts",
            "town",
        )
