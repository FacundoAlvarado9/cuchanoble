# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-04-23 18:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perros', '0013_auto_20171204_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perro',
            name='imagen',
            field=models.ImageField(upload_to='perros'),
        ),
    ]
