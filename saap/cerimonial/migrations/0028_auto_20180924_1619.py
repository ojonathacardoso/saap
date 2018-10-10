# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-09-24 19:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cerimonial', '0027_auto_20180924_1601'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='processo',
            name='proto_cam',
        ),
        migrations.RemoveField(
            model_name='processo',
            name='protocolo',
        ),
        migrations.AddField(
            model_name='processo',
            name='link_camara',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Link para acompanhamento na Câmara'),
        ),
        migrations.AddField(
            model_name='processo',
            name='link_pref_orgao',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Link para acompanhamento na prefeitura ou outro órgão'),
        ),
        migrations.AddField(
            model_name='processo',
            name='materia_cam',
            field=models.CharField(blank=True, max_length=14, null=True, verbose_name='Número da matéria na Câmara'),
        ),
        migrations.AddField(
            model_name='processo',
            name='num_controle',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Número de controle do gabinete'),
        ),
        migrations.AlterField(
            model_name='processo',
            name='titulo',
            field=models.CharField(max_length=200, verbose_name='Título'),
        ),
    ]
