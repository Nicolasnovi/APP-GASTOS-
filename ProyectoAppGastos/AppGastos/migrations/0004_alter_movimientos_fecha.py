# Generated by Django 4.0.3 on 2022-04-07 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppGastos', '0003_alter_movimientos_fecha_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimientos',
            name='Fecha',
            field=models.CharField(max_length=50, verbose_name='Fecha'),
        ),
    ]