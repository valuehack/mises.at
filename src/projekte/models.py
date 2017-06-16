from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify


class Projekte(models.Model):
    id = models.AutoField(primary_key=True)
    slug = models.SlugField()
    titel = models.TextField()
    autor = models.TextField(null=True, blank=True)
    autor_id = models.TextField(null=True, blank=True)
    beschreibung = models.TextField()
    spenden = models.IntegerField()
    ziel = models.IntegerField()
    author = models.ForeignKey('denker.Denker', on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return (str(self.id) + " | " + str(self.author) + ": " + str(self.titel) + " (" + str(self.ziel) + " )")

    class Meta:
        managed = True
        db_table = 'projekte'
        verbose_name = 'Projekt'
        verbose_name_plural = 'Projekte'


def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug and instance.name:
        instance.slug = slugify(instance.titel.rsplit(None, 1)[1])


pre_save.connect(pre_save_receiver, sender=Projekte)


class Stufen(models.Model):
    betrag = models.IntegerField()
    vorteile = models.TextField()
    projekt = models.ForeignKey('projekte.Projekte', on_delete=models.PROTECT)


class Spenden(models.Model):
    Vorname = models.CharField(max_length=100)
    Nachname = models.CharField(max_length=100)
    Email = models.EmailField()
    # Projekt = models.ForeignKey('Projekte', on_delete=models.PROTECT)
    Stufe = models.ForeignKey('Stufen', on_delete=models.PROTECT, null=True)
    Validiert = models.BooleanField(default="False")
    
