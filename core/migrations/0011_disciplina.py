# Generated by Django 5.1.2 on 2024-11-29 18:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0010_professor"),
    ]

    operations = [
        migrations.CreateModel(
            name="Disciplina",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("nome", models.CharField(max_length=45)),
                (
                    "professor",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="core.professor",
                    ),
                ),
            ],
        ),
    ]
