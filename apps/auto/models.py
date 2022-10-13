from django.db import models

from apps.user.models import User
from apps.modelo.models import Modelo


class Auto(models.Model):
    plate = models.CharField(max_length=10)
    mileage = models.PositiveIntegerField(verbose_name= 'Kilometraje')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Auto'
        verbose_name_plural = 'Autos'

    def __str__(self):
        return '%s %s' % (self.plate, self.mileage)
