from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from candidate.models import (
    EducationTitle,
    Employment,
    ExperienceTitle,
    GradeName,
    Profession,
    Technology,
    Town,
)

User = get_user_model()


class VacancyStatus(models.TextChoices):
    """Класс выбора статуса вакансии."""

    active = "active", _("Активная")
    not_active = "not_active", _("Не активная")
    archived = "archived", _("Архивная")
    hidden = "hidden", _("Скрытая")


class Vacancy(models.Model):
    """Модель вакансий."""

    title = models.CharField(
        "Название вакансии",
        max_length=256,
        blank=False,
        default="Новая вакансия",
    )

    company = models.CharField(
        "Название компании",
        max_length=256,
        blank=False,
        default="ООО Рога и копыта",
    )

    country = models.CharField(
        "Страна",
        max_length=256,
        blank=False,
        default="Россия",
    )

    education = models.CharField(
        "Образование",
        max_length=50,
        choices=EducationTitle.choices,
        default=EducationTitle.high_profile,
    )

    author = models.ForeignKey(
        User,
        verbose_name="Автор вакансии",
        related_name="vacancy",
        on_delete=models.CASCADE,
    )

    created_date = models.DateTimeField(
        "Дата создания вакансии",
        auto_now_add=True,
    )

    status = models.CharField(
        "Статус вакансии",
        max_length=16,
        choices=VacancyStatus.choices,
        default=VacancyStatus.active,
    )

    profession = models.ForeignKey(
        Profession,
        verbose_name="Профессия",
        on_delete=models.DO_NOTHING,
        related_name="vacancy",
        blank=False,
        default=None,
    )

    grade = models.CharField(
        "Грейд",
        max_length=16,
        choices=GradeName.choices,
        default=GradeName.junior,
    )

    technology = models.ManyToManyField(
        Technology,
        verbose_name="Стек технологий",
        related_name="vacancy",
        blank=False,
    )

    town = models.ForeignKey(
        Town,
        verbose_name="Город",
        on_delete=models.DO_NOTHING,
        related_name="vacancy",
        blank=False,
        default=None,
    )

    employment = models.ManyToManyField(
        Employment,
        verbose_name="Формат работы",
        related_name="vacancy",
        blank=False,
    )

    experience = models.CharField(
        "Коммерческий опыт",
        max_length=16,
        choices=ExperienceTitle.choices,
        default=ExperienceTitle.no,
    )

    description = models.TextField(
        "Описание вакансии",
        help_text="Добавьте условия вакансии",
        max_length=4000,
        blank=True,
    )

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"

    def __str__(self):
        return self.title
