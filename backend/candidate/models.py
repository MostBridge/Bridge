from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from candidate.validators import validate_file_extension

User = get_user_model()


class GradeName(models.TextChoices):
    """Enum grade."""

    junior = "junior", _("Junior")
    middle = "middle", _("Middle")


class ExperienceTitle(models.TextChoices):
    """Класс выбора опыта."""

    no = "no", _(
        "Нет опыта",
    )
    one = "one", _(
        "1 - 3 года",
    )
    three = "three", _("3 - 6 лет")


class EducationTitle(models.TextChoices):
    """Класс выбора образования."""

    high = "high", _("Высшее")
    high_profile = "high_profile", _("Высшее профильное")
    no_matter = "no_matter", _("Не важно")
    secondary_professional = "secondary_professional", _("Средне-техническое")


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

    slug = models.SlugField(
        verbose_name="Slug",
        max_length=50,
        unique=True,
    )

    class Meta:
        verbose_name = "Profession"
        verbose_name_plural = "Professions"
        ordering = ("name",)

    def __str__(self) -> str:
        return self.name


class Town(models.Model):
    """Модель городов."""

    region = models.CharField(
        verbose_name="Область, регион", max_length=50, null=True, blank=True
    )
    city = models.CharField(
        verbose_name="Название города", max_length=50, blank=False
    )
    district = models.CharField(
        verbose_name="Округ", max_length=50, null=True, blank=True
    )

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"
        ordering = ("city",)

    def __str__(self) -> str:
        return self.city


class Employment(models.Model):
    """Модель формата работы."""

    name = models.CharField(
        verbose_name="Название формата", max_length=50, unique=True
    )
    slug = models.SlugField(
        verbose_name="Slug",
        max_length=50,
        unique=True,
    )

    class Meta:
        verbose_name = "Формат работы"
        verbose_name_plural = "Форматы работ"
        ordering = ("id",)

    def __str__(self):
        return self.name


class Candidate(models.Model):
    """Модель кандидатов."""

    first_name = models.CharField(
        "Имя", max_length=150, blank=False, default=""
    )
    last_name = models.CharField(
        "Фамилия", max_length=150, blank=False, default=""
    )

    experience = models.CharField(
        "Коммерческий опыт",
        max_length=16,
        choices=ExperienceTitle.choices,
        default=ExperienceTitle.no,
    )

    technology = models.ManyToManyField(
        Technology,
        verbose_name="Стек технологий",
        related_name="candidate",
        blank=False,
    )

    employment = models.ManyToManyField(
        Employment,
        verbose_name="Формат работы",
        related_name="candidate",
        blank=False,
    )

    project = models.PositiveSmallIntegerField(
        "Не учебные/pet проекты",
        help_text="Укажите количество не учебных(pet) проектов",
        validators=[MaxValueValidator(50)],
        default=0,
        blank=False,
    )

    portfolio = models.URLField(
        "Портфолио", unique=True, blank=False, default=None
    )

    resume = models.FileField(
        "Резюме",
        upload_to=settings.RESUMES_UPLOAD,
        blank=False,
        validators=[validate_file_extension],
        default=None,
    )

    reviews = models.URLField("Отзывы менторов", blank=True, default=None)

    photo = models.ImageField(
        "Фото кандидата",
        upload_to=settings.PHOTO_UPLOAD,
        blank=True,
    )

    profession = models.ForeignKey(
        Profession,
        verbose_name="Профессия",
        on_delete=models.DO_NOTHING,
        related_name="candidate",
        blank=False,
        default=None,
    )

    grade = models.CharField(
        "Грейд",
        max_length=16,
        choices=GradeName.choices,
        default=GradeName.junior,
    )

    town = models.ForeignKey(
        Town,
        verbose_name="Город",
        on_delete=models.DO_NOTHING,
        related_name="candidates",
        blank=False,
        default=None,
    )

    created_date = models.DateTimeField(
        "Дата создания кандидата",
        auto_now_add=True,
    )

    class Meta:
        verbose_name = "Кандидат"
        verbose_name_plural = "Кандидаты"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Contact(models.Model):
    """Модель контактов кандидата."""

    candidate = models.OneToOneField(
        Candidate,
        on_delete=models.CASCADE,
        verbose_name="Контакты",
        related_name="contacts",
    )
    phone_number = models.CharField(
        "телефон",
        validators=[
            RegexValidator(r"^(8|\+7)[\- ]?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$")
        ],
        max_length=50,
        blank=True,
    )

    email = models.EmailField(
        "email", unique=True, max_length=254, blank=False
    )
    telegram = models.CharField(
        "telegram",
        unique=True,
        max_length=254,
        blank=True,
        validators=[RegexValidator(r"^@\w{5,32}$")],
    )

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"


class View(models.Model):
    """Модель просмотра профиля кандидата."""

    candidate = models.ForeignKey(
        Candidate,
        on_delete=models.CASCADE,
        verbose_name="Кандидат",
        related_name="viewed",
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        related_name="viewed",
    )

    class Meta:
        verbose_name = "Просмотренный кандидат"
        verbose_name_plural = "Просмотренные кандидаты"

    def __str__(self):
        return f"{self.user_id} - {self.candidate_id}"


class Favorite(models.Model):
    """Модель избранных кандидатов."""

    candidate = models.ForeignKey(
        Candidate,
        on_delete=models.CASCADE,
        verbose_name="Кандидат",
        related_name="favorite",
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        related_name="favorite",
    )

    class Meta:
        verbose_name = "Избранный кандидат"
        verbose_name_plural = "Избранные кандидаты"

    def __str__(self):
        return f"{self.user_id} - {self.candidate_id}"
