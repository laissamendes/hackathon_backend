from django.db import models
from .turma import Turma
from uploader.models import Image

class Aluno(models.Model):
    nome = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    turma = models.ForeignKey(Turma, on_delete=models.PROTECT)
    foto = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
    )
    def __str__(self):
        return f"{self.nome}"