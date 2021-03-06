# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-14 13:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('denker', '0009_auto_20170403_1455'),
        ('literatur', '0017_auto_20170413_0958'),
    ]

    operations = [
        migrations.AddField(
            model_name='artikel',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='denker.Denker'),
        ),
        migrations.AddField(
            model_name='buecher',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='denker.Denker'),
        ),
    ]
