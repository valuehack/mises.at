# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-17 13:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orte', '0010_auto_20170417_1317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orte',
            name='denker',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='orte',
            name='denker_neu',
            field=models.ManyToManyField(to='denker.Denker'),
        ),
    ]
