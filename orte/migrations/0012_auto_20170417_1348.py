# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-17 13:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orte', '0011_auto_20170417_1325'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orte',
            old_name='denker',
            new_name='denker_slugs',
        ),
    ]
