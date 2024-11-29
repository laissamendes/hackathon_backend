from django.db import models

from .aluno import Aluno
from .trimestre import Trimestre


class ConselhoClasse(models.Model):
    class StatusChoices(models.TextChoices):
        PENDENTE = "Pendente", "Pendente"
        EM_ANDAMENTO = "Em andamento", "Em andamento"
        FINALIZADO = "Finalizado", "Finalizado"

    aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT)
    data_conselho = models.DateField()
    trimestre = models.ForeignKey(Trimestre, on_delete=models.PROTECT)
    status = models.CharField(max_length=20, choices=StatusChoices.choices, default=StatusChoices.PENDENTE)

    def __str__(self):
        return f"Conselho {self.status}"

    class Meta:
        verbose_name_plural = "Conselhos de Classe"
