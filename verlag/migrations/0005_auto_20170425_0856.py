# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-25 08:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verlag', '0004_auto_20170425_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verlagsprogramm',
            name='denker',
            field=models.ManyToManyField(blank=True, to='denker.Denker'),
        ),
    ]
