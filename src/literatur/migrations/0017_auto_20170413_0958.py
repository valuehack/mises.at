# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-13 09:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('literatur', '0016_auto_20170413_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artikel',
            name='autor',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='artikel',
            name='sprache',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='artikel',
            name='titel',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='buecher',
            name='autor',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='buecher',
            name='sprache',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='buecher',
            name='titel',
            field=models.CharField(max_length=500),
        ),
    ]
