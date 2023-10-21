from django.contrib import admin

from candidate.models import Profession, Technology, Town


@admin.register(Town)
class TownAdmin(admin.ModelAdmin):
    """Управление городами."""

    list_display = ("name",)
    search_fields = ("id",)


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
