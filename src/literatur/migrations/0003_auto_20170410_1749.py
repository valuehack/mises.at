# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-10 15:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('literatur', '0002_auto_20170410_1737'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='artikel',
            table='literatur_artikel',
        ),
        migrations.AlterModelTable(
            name='buecher',
            table='literatur_buecher',
        ),
        migrations.AlterModelTable(
            name='dokumente',
            table='literatur_dokumente',
        ),
    ]