from django.db import models

# Create your models here.
class movimientos(models.Model):
    Fecha= models.CharField('Fecha', max_length=50)
    Categoria= models.CharField('Categoria', max_length=50)
    Importe= models.IntegerField()
    Nota= models.CharField('Nota', max_length=50)
    Tipo_movimiento= models.CharField('Tipo de Movimiento', max_length=50)


class usuario(models.Model):
    ID_Usuario= models.AutoField(primary_key= True)
    Nombre= models.CharField('Nombre', max_length=50)
    Apellido= models.CharField('Apellido', max_length=50)
    Email= models.EmailField('Email',)
    Contraseña = models.CharField('Contraseña', max_length=20)


