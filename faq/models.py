from django.db import models
from autoslug import AutoSlugField


class Glossar(models.Model):
    id = models.AutoField(primary_key=True)
    slug = AutoSlugField(unique=True, max_length=50, populate_from='begriff')
    begriff = models.CharField(max_length=100)
    beschreibung = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return (str(self.id) + " | " + str(self.begriff) + " - " + str(self.slug) + " | " + str(self.beschreibung))

    class Meta:
        verbose_name = 'Begriff'
        verbose_name_plural = 'Begriffe'
