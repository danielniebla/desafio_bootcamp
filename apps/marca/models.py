from django.db import models

class Marca(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    def __str__(self):
        return '%s' % (self.name)