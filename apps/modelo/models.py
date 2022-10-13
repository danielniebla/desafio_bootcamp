from django.db import models

from apps.marca.models import Marca

class Modelo(models.Model):
    name = models.CharField(max_length= 30)
    brand = models.ForeignKey(Marca,on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Modelo'
        verbose_name_plural = 'Modelos'

    def __str__(self):
        return '%s ' % (self.name)