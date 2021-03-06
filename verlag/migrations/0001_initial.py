# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-25 08:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('framework', '0005_auto_20170425_0808'),
    ]

    state_operations = [
        migrations.CreateModel(
            name='Verlagsprogramm',
            fields=[
                ('n', models.AutoField(primary_key=True, serialize=False)),
                ('id', models.TextField()),
                ('title', models.TextField()),
                ('desc', models.TextField()),
                ('author', models.TextField()),
                ('link', models.TextField()),
            ],
            options={
                'db_table': 'verlag_verlagsprogramm',
                'managed': True,
            },
        ),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(state_operations=state_operations)
    ]
