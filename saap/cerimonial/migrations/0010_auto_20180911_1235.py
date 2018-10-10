# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-09-11 15:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cerimonial', '0009_auto_20180911_1222'),
    ]

    operations = [
        migrations.AddField(
            model_name='processo',
            name='oficio_cam',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='Ofício enviado pela Câmara'),
        ),
        migrations.AddField(
            model_name='processo',
            name='oficio_orgao',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='Ofício recebido de outro órgão'),
        ),
        migrations.AddField(
            model_name='processo',
            name='oficio_pref',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='Ofício recebido da Prefeitura'),
        ),
    ]