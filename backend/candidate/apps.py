from django.apps import AppConfig


class CandidateConfig(AppConfig):
    """AppConfig приложения candidate."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "candidate"
    verbose_name = "Кандидаты"
