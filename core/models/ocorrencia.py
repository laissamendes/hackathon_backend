from django.db import models
from .user import User
from .aluno import Aluno


class Ocorrencia(models.Model):
    class CategoriaOcorrencia(models.IntegerChoices):
          ATRASO = 1, "Atraso"
          SEM_UNIFORME = 2, "Sem uniforme"
          REUNIAO_NUPE = 3, "Reunião no NUPE"
          OUTRO = 4, "Outro"
    
    descricao = models.CharField(max_length=255, blank=True, null=True)
    aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    data_criacao = models.DateField()
    categoria_ocorrencia = models.IntegerField(choices=CategoriaOcorrencia.choices,  default=CategoriaOcorrencia.ATRASO)


    def __str__(self):
        return f"{self.categoria_ocorrencia}"

class Meta:
        verbose_name = "Ocorrência"
        verbose_name_plural = "Ocorrências"