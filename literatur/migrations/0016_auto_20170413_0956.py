# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-13 09:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('literatur', '0015_auto_20170413_0953'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dokumente',
            options={'managed': True, 'verbose_name': 'Dokument', 'verbose_name_plural': 'Dokumente'},
        ),
    ]
