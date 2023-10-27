# Generated by Django 4.2.6 on 2023-10-27 04:10

import candidate.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("candidate", "0004_candidate_experience_candidate_first_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="candidate",
            name="photo",
            field=models.ImageField(
                blank=True, upload_to="photo/", verbose_name="Фото кандидата"
            ),
        ),
        migrations.AlterField(
            model_name="candidate",
            name="resume",
            field=models.FileField(
                default=None,
                upload_to="resumes/",
                validators=[candidate.validators.validate_file_extension],
                verbose_name="Резюме",
            ),
        ),
    ]
