from django.contrib import admin

from vacancy.models import Vacancy


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    """Управление пользователями."""

    list_display = (
        "pk",
        "title",
        "profession",
    )
    search_fields = ("profession",)
