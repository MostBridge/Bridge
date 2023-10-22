from django.contrib import admin

from candidate.models import Candidate, Contact, Profession, Technology, Town


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
        "contacts",
        "town",
    )
    inlines = [ContactInline]
