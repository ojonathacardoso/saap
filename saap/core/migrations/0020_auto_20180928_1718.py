# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-09-28 20:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20180921_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bairro',
            name='nome',
            field=models.CharField(max_length=254, verbose_name='Bairro'),
        ),
    ]
