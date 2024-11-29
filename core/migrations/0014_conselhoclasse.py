# Generated by Django 5.1.2 on 2024-11-29 18:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0013_remove_trimestre_nome_trimestre_periodo"),
    ]

    operations = [
        migrations.CreateModel(
            name="ConselhoClasse",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("data_conselho", models.DateField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Pendente", "Pendente"),
                            ("Em andamento", "Em andamento"),
                            ("Finalizado", "Finalizado"),
                        ],
                        default="Pendente",
                        max_length=20,
                    ),
                ),
                ("aluno", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="core.aluno")),
                ("trimestre", models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to="core.trimestre")),
            ],
            options={
                "verbose_name_plural": "Conselhos de Classe",
            },
        ),
    ]
