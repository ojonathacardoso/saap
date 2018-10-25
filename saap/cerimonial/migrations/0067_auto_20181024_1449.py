# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-10-24 17:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cerimonial', '0066_auto_20181022_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='telefone',
            name='ramal',
            field=models.CharField(blank=True, max_length=40, verbose_name='Ramal'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='complemento',
            field=models.CharField(blank=True, default='', max_length=15, verbose_name='Complemento'),
        ),
    ]
