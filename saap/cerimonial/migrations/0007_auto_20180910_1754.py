# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-09-10 20:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cerimonial', '0006_auto_20180830_1547'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='email',
            options={'verbose_name': 'E-mail', 'verbose_name_plural': 'E-mails'},
        ),
        migrations.AlterModelOptions(
            name='emailperfil',
            options={'verbose_name': 'E-mail do perfil', 'verbose_name_plural': 'E-mails do perfil'},
        ),
        migrations.RemoveField(
            model_name='assuntoprocesso',
            name='workspace',
        ),
        migrations.AlterField(
            model_name='contato',
            name='nivel_instrucao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contato_set', to='cerimonial.NivelInstrucao', verbose_name='Nível de instrução'),
        ),
        migrations.AlterField(
            model_name='contato',
            name='nome_social',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='Nome social'),
        ),
        migrations.AlterField(
            model_name='contato',
            name='observacoes',
            field=models.TextField(blank=True, default='', verbose_name='Outras observações sobre o contato'),
        ),
        migrations.AlterField(
            model_name='dependente',
            name='data_nascimento',
            field=models.DateField(blank=True, null=True, verbose_name='Data de nascimento'),
        ),
        migrations.AlterField(
            model_name='dependente',
            name='nome_social',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='Nome social'),
        ),
        migrations.AlterField(
            model_name='email',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='observacoes',
            field=models.TextField(blank=True, default='', verbose_name='Outras observações sobre o endereço'),
        ),
        migrations.AlterField(
            model_name='processo',
            name='urgente',
            field=models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=True, verbose_name='Urgente'),
        ),
        migrations.AlterField(
            model_name='telefone',
            name='permissao',
            field=models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=True, help_text='Permite que a Câmara entre em contato neste telefone?', verbose_name='Permissão:'),
        ),
    ]
