# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-17 13:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('denker', '0010_auto_20170414_1518'),
        ('orte', '0008_auto_20170417_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='orte',
            name='denker_neu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='denker.Denker'),
        ),
        migrations.AlterField(
            model_name='orte',
            name='denker',
            field=models.CharField(max_length=200),
        ),
    ]
