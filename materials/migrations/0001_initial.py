# Generated by Django 4.2.7 on 2023-12-05 07:56

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Material",
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
                ("title", models.CharField(max_length=100, verbose_name="название")),
                ("body", models.TextField(verbose_name="содержимое")),
            ],
        ),
    ]
