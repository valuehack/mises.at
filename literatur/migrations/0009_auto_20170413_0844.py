# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-13 08:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('literatur', '0008_auto_20170413_0829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artikel',
            name='slug',
            field=models.SlugField(allow_unicode=True, max_length=250),
        ),
    ]
