# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-04 09:15
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Glossar',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from=('begriff',), unique=True)),
                ('begriff', models.CharField(max_length=100)),
                ('beschreibung', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Glossar',
                'verbose_name_plural': 'Begriffe',
            },
        ),
    ]
