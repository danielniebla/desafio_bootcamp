from django.db import models

from apps.auto.models import Auto

class Mantenimiento(models.Model):
    mileage = models.PositiveSmallIntegerField(verbose_name='Kilometraje')
    description = models.CharField(max_length=320)
    cost = models.PositiveSmallIntegerField(verbose_name='Costo')
    date = models.DateField(verbose_name='Fecha de llegada')
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Mantenimiento'
        verbose_name_plural = 'Mantenimientos'

    def __str__(self):
        return '%s %s %s %s' % (self.mileage ,self.description, self.cost, self.date)

