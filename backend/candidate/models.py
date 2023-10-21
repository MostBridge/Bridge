from django.db import models


class Candidate(models.Model):
    """Модель кандидатов."""

    pass


class Favorite(models.Model):
    """Модель избранных кандидатов."""

    pass


class Technology(models.Model):
    """Модель стека технологий."""

    name = models.CharField(
        verbose_name="Название технологии", max_length=50, unique=True
    )
    slug = models.SlugField(
        verbose_name="Slug",
        max_length=50,
        unique=True,
    )

    class Meta:
        verbose_name = "Technology"
        verbose_name_plural = "Technologies"
        ordering = ("name",)

    def __str__(self) -> str:
        return self.name


class Profession(models.Model):
    """Модель профессий."""

    name = models.CharField(
        verbose_name="Название профессии", max_length=50, unique=True
    )

    class Meta:
        verbose_name = "Profession"
        verbose_name_plural = "Professions"
        ordering = ("name",)

    def __str__(self) -> str:
        return self.name


class Town(models.Model):
    """Модель городов."""

    name = models.CharField(
        verbose_name="Название города", max_length=50, unique=True
    )

    class Meta:
        verbose_name = "Town"
        verbose_name_plural = "Towns"
        ordering = ("name",)

    def __str__(self) -> str:
        return self.name
