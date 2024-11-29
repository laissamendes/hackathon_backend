from django.db import models
from .turma import Turma

class Aluno(models.Model):
    nomeAluno = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    turma = models.ForeignKey(Turma, on_delete=models.PROTECT)