# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-17 13:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('denker', '0010_auto_20170414_1518'),
        ('orte', '0009_auto_20170417_1309'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orte',
            name='denker_neu',
        ),
        migrations.AddField(
            model_name='orte',
            name='denker_neu',
            field=models.ManyToManyField(blank=True, null=True, to='denker.Denker'),
        ),
    ]
