from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Управление пользователями."""

    list_display = (
        "pk",
        "username",
        "email",
    )
    search_fields = ("username",)
    list_editable = (
        "username",
        "email",
    )
