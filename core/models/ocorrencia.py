from django.db import models
from .user import User
from .aluno import Aluno


class Ocorrencia(models.Model):
    descricao = models.CharField(max_length=255)
    aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    data_criacao = models.DateField()
    class CategoriaOcorrencia(models.IntegerChoices):
          ATRASO = 1, "Atraso"
          SEM_UNIFORME = 2, "Sem uniforme"
          REUNIAO_NUPE = 3, "Reunião no NUPE"
          OUTRO = 4, "Outro"

class Meta:
        verbose_name = "Ocorrência"
        verbose_name_plural = "Ocorrências"