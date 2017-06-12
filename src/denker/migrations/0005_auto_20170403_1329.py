# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-03 13:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('denker', '0004_auto_20170331_1327'),
    ]

    database_operations = [
        migrations.AlterModelTable('Artikel', 'framework_artikel'),
        migrations.AlterModelTable('Buecher', 'framework_buecher'),
        migrations.AlterModelTable('Dokumente', 'framework_dokumente'),
        migrations.AlterModelTable('Ereignisse', 'framework_ereignisse'),
        migrations.AlterModelTable('Orte', 'framework_orte'),
        migrations.AlterModelTable('Projekte', 'framework_projekte'),
        migrations.AlterModelTable('StatischeInhalte', 'framework_statische_inhalte'),
        migrations.AlterModelTable('Verlagsprogramm', 'framework_verlagsprogramm'),
        migrations.AlterModelTable('Zitate', 'framework_zitate'),
    ]

    state_operations = [
        migrations.DeleteModel('Artikel'),
        migrations.DeleteModel('Buecher'),
        migrations.DeleteModel('Dokumente'),
        migrations.DeleteModel('Ereignisse'),
        migrations.DeleteModel('Orte'),
        migrations.DeleteModel('Projekte'),
        migrations.DeleteModel('StatischeInhalte'),
        migrations.DeleteModel('Verlagsprogramm'),
        migrations.DeleteModel('Zitate'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=database_operations,
            state_operations=state_operations)
    ]