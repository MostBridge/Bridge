from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from candidate.models import (
    Candidate,
    Contact,
    Employment,
    Favorite,
    Profession,
    Technology,
    Town,
)
from vacancy.models import Vacancy


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
    is_favorited = serializers.SerializerMethodField()

    def get_is_favorited(self, obj):
        """Метод получения избранных кандидатов."""
        current_user = self.context["request"].user
        return obj.favorite.filter(user=current_user).exists()

    class Meta:
        model = Candidate
        fields = (
            "id",
            "first_name",
            "last_name",
            "experience",
            "employment",
            "project",
            "portfolio",
            "resume",
            "reviews",
            "contacts",
            "town",
            "profession",
            "grade",
            "employment",
            "photo",
            "is_favorited",
        )
        read_only_fields = (
            "id",
            "first_name",
            "last_name",
            "experience",
            "employment",
            "project",
            "portfolio",
            "resume",
            "reviews",
            "contacts",
            "town",
            "profession",
            "grade",
            "employment",
            "photo",
            "is_favorited",
        )


class CandidateShortSerializer(CandidateSerializer):
    """Укороченный сериализатор кандидата."""

    class Meta(CandidateSerializer.Meta):
        fields = ("id",)
        read_only_fields = ("id",)


class FavoriteSerializer(serializers.ModelSerializer):
    """Сериализатор добавления в избранное."""

    class Meta:
        model = Favorite
        fields = ("candidate", "user")

    def validate(self, attrs):
        """Валидация избранных кандидатов."""
        candidate = attrs.get("candidate")
        method = self.context.get("method")
        current_user = attrs.get("user")
        if method == "POST":
            if candidate.favorite.filter(user=current_user).exists():
                raise serializers.ValidationError(
                    {"errors": "Кандидат уже в избранном!"}
                )
        elif method == "DELETE":
            if not candidate.favorite.filter(user=current_user).exists():
                raise serializers.ValidationError(
                    {"errors": "Кандидата нет в избранном!"}
                )
        return attrs


class VacancySerializer(serializers.ModelSerializer):
    """Сериализатор вакансий."""

    class Meta:
        model = Vacancy

        fields = (
            "id",
            "title",
            "company",
            "country",
            "education",
            "status",
            "author",
            "grade",
            "profession",
            "town",
            "employment",
            "experience",
            "description",
        )
        read_only_fields = (
            "id",
            "title",
            "company",
            "country",
            "education",
            "status",
            "author",
            "grade",
            "profession",
            "town",
            "employment",
            "experience",
            "description",
        )
