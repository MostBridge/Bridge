# Generated by Django 4.2.6 on 2023-10-27 04:10

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={
                "ordering": ("id",),
                "verbose_name": "Рекрутер",
                "verbose_name_plural": "Рекрутеры",
            },
        ),
    ]
