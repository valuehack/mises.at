# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-14 17:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('literatur', '0018_auto_20170414_1319'),
    ]

    operations = [
        migrations.AddField(
            model_name='artikel',
            name='typ',
            field=models.CharField(default='Artikel', max_length=50),
        ),
        migrations.AddField(
            model_name='buecher',
            name='typ',
            field=models.CharField(default='Buch', max_length=50),
        ),
    ]