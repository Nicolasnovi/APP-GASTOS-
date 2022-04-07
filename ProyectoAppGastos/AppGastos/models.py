from django.db import models

# Create your models here.
class movimientos(models.Model):
    Fecha= models.CharField('Fecha', max_length=50)
    Categoria= models.CharField('Categoria', max_length=50)
    Importe= models.IntegerField()
    Nota= models.CharField('Nota', max_length=50)
    Tipo_movimiento= models.CharField('Tipo de Movimiento', max_length=50)

