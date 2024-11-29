from django.db import models

from .trimestre import Trimestre
from .turma import Turma


class PreConselho(models.Model):
    turma = models.ForeignKey(
        Turma,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
    )
    trimestre = models.ForeignKey(
        Trimestre,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
    )
    descricao_trimestre = models.CharField(max_length=1000)

    def __str__(self):
        return f"Pré-Conselho de {self.turma} - Trimestre {self.trimestre}"


class Meta:
    verbose_name = "Pré-Conselho"
    verbose_name_plural = "Pré-Conselhos"
