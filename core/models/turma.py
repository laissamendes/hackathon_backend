from django.db import models

class Turma(models.Model):
    nome = models.CharField(max_length=6)