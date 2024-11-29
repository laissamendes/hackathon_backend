# Generated by Django 5.1.2 on 2024-11-29 19:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0015_alter_professor_email_preconselho"),
    ]

    operations = [
        migrations.CreateModel(
            name="AlunoTemDisciplina",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "aluno",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="core.aluno",
                    ),
                ),
                (
                    "disciplina",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="core.disciplina",
                    ),
                ),
            ],
        ),
    ]
