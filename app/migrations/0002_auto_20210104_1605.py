# Generated by Django 3.1.5 on 2021-01-04 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="recipe",
            name="content",
            field=models.TextField(default="", null=True),
        ),
        migrations.AddField(
            model_name="recipe",
            name="summary",
            field=models.CharField(default="", max_length=200, null=True),
        ),
    ]
