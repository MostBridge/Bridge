import os

from django.core.exceptions import ValidationError


def validate_file_extension(data):
    """Валидация форматов файлов резюме."""
    ext = os.path.splitext(data.name)[-1]
    valid_extensions = (
        ".pdf",
        ".doc",
        ".docx",
    )
    if ext.lower() not in valid_extensions:
        raise ValidationError(
            "Для загрузки резюме доступны форматы:"
            f" {', '.join(valid_extensions)}"
        )
