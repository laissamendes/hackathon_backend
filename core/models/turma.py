from django.db import models

class Turma(models.Model):
    nome = models.CharField(max_length=6)

    def __str__(self):
        return f"{self.nome}"