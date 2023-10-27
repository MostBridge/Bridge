from django.apps import AppConfig


class VacancyConfig(AppConfig):
    """AppConfig приложения vacancy."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "vacancy"
    verbose_name = "Вакансии"
