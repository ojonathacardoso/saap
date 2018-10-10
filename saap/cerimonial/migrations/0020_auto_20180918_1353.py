# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-09-18 16:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20180918_1345'),
        ('cerimonial', '0019_auto_20180918_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='endereco',
            name='estado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='endereco_set', to='core.Estado', verbose_name='Estado'),
        ),
        migrations.AddField(
            model_name='localtrabalho',
            name='estado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='localtrabalho_set', to='core.Estado', verbose_name='Estado'),
        ),
    ]