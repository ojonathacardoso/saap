# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-09-26 19:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import saap.utils
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('cerimonial', '0047_auto_20180926_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='bairro',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='municipio', chained_model_field='municipio', default=5, on_delete=django.db.models.deletion.CASCADE, to='core.Bairro', verbose_name='Bairro'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='cep',
            field=models.CharField(default='', max_length=9, validators=[saap.utils.validate_CEP], verbose_name='CEP'),
        ),
    ]
