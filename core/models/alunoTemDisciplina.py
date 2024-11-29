from django.db import models

from .aluno import Aluno
from .disciplina import Disciplina

class AlunoTemDisciplina(models.Model):
    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        default=None,
    )
    disciplina = models.ForeignKey(
        Disciplina,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return f"{self.aluno} - {self.disciplina}"

