from django.db import models


class Professor(models.Model):
    email = models.EmailField(max_length=255, blank=True, null=True)
    nome = models.CharField(max_length=45)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Professores"