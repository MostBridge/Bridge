from django.contrib.auth import get_user_model
from django_filters import rest_framework as filters

from candidate.models import (
    Candidate,
    Technology,
    Town,
    Profession,
    GradeName,
    Employment
)

User = get_user_model()


class CandidateFilter(filters.FilterSet):
    """Фильтры для запросов."""

    town = filters.ModelChoiceFilter(
        field_name="town__city",
        to_field_name="city",
        queryset=Town.objects.all(),
    )
    profession = filters.ModelChoiceFilter(
        field_name="profession",
        to_field_name="slug",
        queryset=Profession.objects.all(),
    )
    grade = filters.ChoiceFilter(
        field_name="grade",
        choices=GradeName.choices
    )
    employment = filters.ModelMultipleChoiceFilter(
        field_name='employment__slug',
        to_field_name='slug',
        queryset=Employment.objects.all(),
    )
    technology = filters.ModelMultipleChoiceFilter(
        field_name='technology__slug',
        to_field_name='slug',
        queryset=Technology.objects.all(),
    )

    class Meta:
        model = Candidate
        fields = ("town", "profession", "grade", "employment", "technology")
