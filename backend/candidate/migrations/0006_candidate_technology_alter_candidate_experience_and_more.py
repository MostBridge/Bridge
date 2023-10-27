# Generated by Django 4.2.6 on 2023-10-27 09:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("candidate", "0005_profession_slug_alter_candidate_photo_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="candidate",
            name="technology",
            field=models.ManyToManyField(
                related_name="candidate",
                to="candidate.technology",
                verbose_name="Стек технологий",
            ),
        ),
        migrations.AlterField(
            model_name="candidate",
            name="experience",
            field=models.CharField(
                choices=[
                    ("no", "Нет опыта"),
                    ("one", "1 - 3 года"),
                    ("three", "3 - 6 лет"),
                ],
                default="no",
                max_length=16,
                verbose_name="Коммерческий опыт",
            ),
        ),
        migrations.AlterField(
            model_name="candidate",
            name="grade",
            field=models.CharField(
                choices=[("junior", "Junior"), ("middle", "Middle")],
                default="junior",
                max_length=16,
                verbose_name="Грейд",
            ),
        ),
    ]
