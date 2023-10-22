from candidate.models import Profession, Technology, Town
from rest_framework import serializers


class TechnologySerializer(serializers.ModelSerializer):
    """Сериализация для технологий."""

    class Meta:
        model = Technology
        fields = ("id", "name", "slug")
        read_only_fields = ("name", "slug")


class TownSerializer(serializers.ModelSerializer):
    """Сериализация для города."""

    class Meta:
        model = Town
        fields = ("id", "name")
        read_only_fields = ("name",)


class ProfessionSerializer(serializers.ModelSerializer):
    """Сериализация для профессии."""

    class Meta:
        model = Profession
        fields = ("id", "name")
        read_only_fields = ("name",)
