# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-10-03 17:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cerimonial', '0058_processo_data_protocolo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='permissao',
        ),
        migrations.RemoveField(
            model_name='telefone',
            name='permissao',
        ),
        migrations.AlterField(
            model_name='email',
            name='contato',
            field=models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=True, help_text='Autorizado para contato do gabinete', verbose_name='Contato'),
        ),
        migrations.AlterField(
            model_name='email',
            name='principal',
            field=models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=True, verbose_name='Principal?'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='contato',
            field=models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=True, help_text='Autorizado para contato do gabinete', verbose_name='Contato'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='principal',
            field=models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=True, verbose_name='Principal?'),
        ),
        migrations.AlterField(
            model_name='localtrabalho',
            name='principal',
            field=models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=True, verbose_name='Principal?'),
        ),
        migrations.AlterField(
            model_name='telefone',
            name='contato',
            field=models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=True, help_text='Autorizado para contato do gabinete', verbose_name='Contato'),
        ),
    ]
