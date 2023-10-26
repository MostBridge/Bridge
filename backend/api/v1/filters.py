from django.contrib.auth import get_user_model
from django_filters import rest_framework as filters

from candidate.models import Candidate, Town, Profession

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

    class Meta:
        model = Candidate
        fields = ("town", "profession", "grade")
