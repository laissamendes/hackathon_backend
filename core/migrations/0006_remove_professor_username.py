# Generated by Django 5.1.2 on 2024-11-29 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_professor"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="professor",
            name="username",
        ),
    ]