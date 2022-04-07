# Generated by Django 4.0.3 on 2022-04-07 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppGastos', '0007_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='objetivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Objetivo', models.CharField(max_length=30, verbose_name='Objetivo')),
                ('MontoDelObjetivo', models.IntegerField()),
                ('Fecha', models.CharField(max_length=8, verbose_name='Fecha')),
                ('Observacion', models.CharField(max_length=100, verbose_name='Observacion')),
            ],
        ),
    ]
