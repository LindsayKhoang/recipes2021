# Generated by Django 3.1.5 on 2021-01-04 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_auto_20210104_1605"),
    ]

    operations = [
        migrations.CreateModel(
            name="Ingredient",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name_singular",
                    models.CharField(default="", max_length=200, null=True),
                ),
                (
                    "name_plural",
                    models.CharField(default="", max_length=200, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Unit",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(default="", max_length=200, null=True),
                ),
            ],
        ),
    ]
