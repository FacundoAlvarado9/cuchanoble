# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-14 01:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perros', '0008_auto_20171112_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='perro',
            name='edad',
            field=models.CharField(choices=[('Cachorro', 'CACHORRO'), ('Adulto', 'ADULTO')], max_length=7, null=True),
        ),
        migrations.AddField(
            model_name='perro',
            name='sexo',
            field=models.CharField(choices=[('Macho', 'MACHO'), ('Hembra', 'Hembra')], max_length=5, null=True),
        ),
    ]
