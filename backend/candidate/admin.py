from django.contrib import admin

from candidate.models import (
    Candidate,
    Contact,
    Employment,
    Profession,
    Technology,
    Town,
)


@admin.register(Town)
class TownAdmin(admin.ModelAdmin):
    """Управление городами."""

    list_display = ("region", "city", "district")
    search_fields = ("city",)


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    """Управление технологиями."""

    list_display = ("name", "slug")
    search_fields = ("id",)


@admin.register(Employment)
class EmploymentAdmin(admin.ModelAdmin):
    """Управление форматом работы."""

    list_display = ("name", "slug")
    search_fields = ("id",)


@admin.register(Profession)
class ProfessionAdmin(admin.ModelAdmin):
    """Управление профессиями."""

    list_display = ("name",)
    search_fields = ("id",)


class ContactInline(admin.TabularInline):
    """Управление контактами."""

    model = Contact


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    """Управление кандидатами."""

    list_display = (
        "full_name",
        "profession",
        "town",
    )
    inlines = [ContactInline]

    @admin.display(description="Полное имя")
    def full_name(self, obj):
        """Добавление полного имени."""
        return f"{obj.first_name} {obj.last_name}"
