from django.db import models

from .aluno import Aluno
from .disciplina import Disciplina
from .conselhoClasse import ConselhoClasse
from .trimestre import Trimestre

class Nota(models.Model):
    nota = models.DecimalField(max_digits=3, decimal_places=1)
    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.PROTECT,
        default=None,
    )
    disciplina = models.ForeignKey(
        Disciplina,
        on_delete=models.PROTECT,
        default=None,
    )
    conselhoClasse = models.ForeignKey(
        ConselhoClasse,
        on_delete=models.PROTECT,
        default=None,
    )
    trimestre = models.ForeignKey(
        Trimestre,
        on_delete=models.PROTECT,
        default=None,
    )

    def __str__(self):
        return f"{self.aluno} - {self.disciplina}"