# Generated by Django 4.2.4 on 2023-09-06 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0003_team"),
    ]

    operations = [
        migrations.CreateModel(
            name="main_bg",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("img", models.ImageField(upload_to="imgs")),
            ],
        ),
    ]
