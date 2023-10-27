from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from candidate.models import (
    Candidate,
    Contact,
    EducationTitle,
    Employment,
    ExperienceTitle,
    Favorite,
    GradeName,
    Profession,
    Technology,
    Town,
)
from users.serializers import UserSerializer
from vacancy.models import Vacancy, VacancyStatus


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
    is_viewed = serializers.SerializerMethodField()

    def get_is_favorited(self, obj):
        """Метод получения избранных кандидатов."""
        current_user = self.context["request"].user
        return obj.favorite.filter(user=current_user).exists()

    def get_is_viewed(self, obj):
        """Метод получения просмотренных кандидатов."""
        current_user = self.context["request"].user
        return obj.viewed.filter(user=current_user).exists()

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
            "is_viewed",
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
            "is_viewed",
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


class FavoriteDownloadSerializers(FavoriteSerializer):
    """Сериализатор скачивания резюме избранных кандидатов."""

    class Meta(FavoriteSerializer.Meta):
        read_only_fields = ("candidate",)

    def validate(self, attrs):
        """Валидация избранных кандидатов."""
        current_user = attrs.get("user")
        favorite = current_user.favorite.all()
        if not favorite:
            raise serializers.ValidationError(
                {"errors": "В избранном нет кандидатов!"}
            )
        return favorite


class VacancySerializer(serializers.ModelSerializer):
    """Сериализатор вакансий."""

    title = serializers.CharField()
    company = serializers.CharField()
    country = serializers.CharField()
    education = serializers.ChoiceField(choices=EducationTitle.choices)
    status = serializers.ChoiceField(choices=VacancyStatus.choices)
    grade = serializers.ChoiceField(choices=GradeName.choices)
    profession = ProfessionSerializer()
    experience = serializers.ChoiceField(choices=ExperienceTitle.choices)
    author = UserSerializer(default=serializers.CurrentUserDefault())
    town = TownSerializer()
    employment = EmploymentSerializer(many=True)
    technology = TechnologySerializer(many=True)
    description = serializers.CharField(max_length=4000)

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
            "technology",
            "created_date",
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
            "technology",
            "created_date",
        )


class VacancySerializerCreate(VacancySerializer):
    """Сериализатор создания вакансии."""

    profession = serializers.PrimaryKeyRelatedField(
        queryset=Profession.objects.all()
    )
    technology = serializers.PrimaryKeyRelatedField(
        queryset=Technology.objects.all(), many=True
    )
    town = serializers.PrimaryKeyRelatedField(
        queryset=Town.objects.all(),
    )
    employment = serializers.PrimaryKeyRelatedField(
        queryset=Employment.objects.all(), many=True
    )

    class Meta(VacancySerializer.Meta):
        read_only_fields = (
            "id",
            "author",
        )
