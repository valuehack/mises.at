# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 12:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('denker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='denker',
            name='geburt',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='denker',
            name='tod',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='denkeralt',
            name='geburt',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='denkeralt',
            name='tod',
            field=models.DateField(blank=True, null=True),
        ),
    ]
