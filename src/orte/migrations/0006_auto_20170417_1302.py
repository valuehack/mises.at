# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-17 13:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orte', '0005_auto_20170417_1256'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orte',
            options={'managed': True, 'verbose_name': 'Ort', 'verbose_name_plural': 'Orte'},
        ),
        migrations.AlterField(
            model_name='orte',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, max_length=250, null=True, unique=True),
        ),
    ]