from django.db import models


class Trimestre(models.Model):
    class Periodo(models.IntegerChoices):
          PRIMEIRO = 1, "Primeiro"
          SEGUNDO = 2, "Segundo"
          TERCEIRO = 3, "Terceiro"
    periodo = models.IntegerField(choices=Periodo.choices,  default=Periodo.PRIMEIRO)
    def __str__(self):
        return f"{self.periodo}"

    class Meta:
        verbose_name_plural = "Trimestres"