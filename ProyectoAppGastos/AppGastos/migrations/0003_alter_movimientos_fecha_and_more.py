# Generated by Django 4.0.3 on 2022-04-07 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppGastos', '0002_rename_tipo_gasto_movimientos_tipo_movimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimientos',
            name='Fecha',
            field=models.DateField(max_length=50, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='movimientos',
            name='Tipo_movimiento',
            field=models.CharField(max_length=50, verbose_name='Tipo de Movimiento'),
        ),
    ]