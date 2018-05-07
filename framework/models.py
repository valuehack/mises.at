from __future__ import unicode_literals
from django.db import models


class Ereignisse(models.Model):
    n = models.AutoField(primary_key=True)
    id = models.TextField()
    ereignis = models.TextField()
    jahr = models.IntegerField()
    denker = models.TextField()
    text_de = models.TextField()
    text_en = models.TextField()

    class Meta:
        managed = True
        db_table = 'ereignisse'


class StatischeInhalte(models.Model):
    n = models.AutoField(primary_key=True)
    id = models.TextField()
    info = models.TextField()

    class Meta:
        managed = True
        db_table = 'statische_inhalte'


class Zitate(models.Model):
    n = models.AutoField(primary_key=True)
    id = models.TextField()
    autor = models.TextField()
    text = models.TextField()
    quelle = models.TextField()

    class Meta:
        managed = True
        db_table = 'zitate'
