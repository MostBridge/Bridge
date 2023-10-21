from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

User = get_user_model()


class UserRegistrationSerializer(UserCreateSerializer):
    """Сериализатор регистрации пользователя."""

    email = serializers.EmailField(
        max_length=254,
        required=True,
        validators=(
            UniqueValidator(
                queryset=User.objects.all(),
                message="Пользователь с таким email уже существует",
            ),
        ),
    )
    username = serializers.CharField(
        max_length=150,
        required=True,
        validators=(
            RegexValidator(r"^[\w.@+-]+$", message="Проверьте username!"),
            UniqueValidator(
                queryset=User.objects.all(),
                message="Пользователь с таким username уже существует",
            ),
        ),
    )
    password = serializers.CharField(max_length=150, write_only=True)

    class Meta(UserCreateSerializer.Meta):
        fields = (
            "id",
            "email",
            "username",
            "first_name",
            "last_name",
            "password",
        )
        read_only_fields = ("id",)


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор авторизованного пользователя."""

    class Meta:
        model = User
        fields = (
            "email",
            "id",
            "username",
            "first_name",
            "last_name",
        )
        read_only_fields = (
            "email",
            "id",
            "username",
            "first_name",
            "last_name",
        )
