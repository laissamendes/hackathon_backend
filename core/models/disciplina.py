from django.db import models

from .professor import Professor


class Disciplina(models.Model):
    nome = models.CharField(max_length=45)
    professor = models.ForeignKey( Professor,on_delete=models.PROTECT, null=True, blank=True, default=None)

    def __str__(self):
        return self.nome


class Meta:
    verbose_name_plural = "Disciplinas"