# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-10-03 19:27
from __future__ import unicode_literals

from django.db import migrations
import exclusivebooleanfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cerimonial', '0060_auto_20181003_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telefone',
            name='permite_contato',
            field=exclusivebooleanfield.fields.ExclusiveBooleanField(),
        ),
    ]
