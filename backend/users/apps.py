from django.apps import AppConfig


class UsersConfig(AppConfig):
    """AppConfig приложения users."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "users"
    verbose_name = "Рекрутеры"
