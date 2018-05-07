from django.db import models
from django.utils.text import slugify


class Artikel(models.Model):
    id = models.AutoField(primary_key=True)
    slug = models.SlugField(allow_unicode=True, unique=True, max_length=250, null=True, blank=True)
    titel = models.CharField(max_length=500)
    jahr = models.IntegerField()
    sprache = models.CharField(max_length=50)
    autor = models.CharField(max_length=250)
    link = models.TextField(null=True, blank=True)
    quelle = models.TextField(null=True, blank=True)
    typ = models.CharField(max_length=50, default="Artikel")
    author = models.ForeignKey('denker.Denker', on_delete=models.PROTECT, null=True, blank=True)
    
    def __str__(self):
        return (str(self.id) + " | " + str(self.author) + ": " + str(self.titel) + " (" + str(self.jahr) + " )")

    class Meta:
        managed = True
        db_table = 'artikel'
        verbose_name = 'Artikel'
        verbose_name_plural = 'Artikel'
        
    def pre_save_receiver(sender, instance, *args, **kwargs):
        if not instance.slug and instance.titel:
            instance.slug = slugify(instance.titel.rsplit(None, 1)[1])


class Buecher(models.Model):
    id = models.AutoField(primary_key=True)
    slug = models.SlugField(allow_unicode=True, unique=True, max_length=250, null=True, blank=True)
    titel = models.CharField(max_length=500)
    jahr = models.IntegerField()
    sprache = models.CharField(max_length=50)
    autor = models.CharField(max_length=250)
    link = models.TextField(null=True, blank=True)
    quelle = models.TextField(null=True, blank=True)
    typ = models.CharField(max_length=50, default="Buch")
    author = models.ForeignKey('denker.Denker', on_delete=models.PROTECT, null=True, blank=True)
    
    def __str__(self):
        return (str(self.id) + " | " + str(self.author) + ": " + str(self.titel) + " (" + str(self.jahr) + " )")

    class Meta:
        managed = True
        db_table = 'buecher'
        verbose_name = 'Buch'
        verbose_name_plural = 'Buecher'
        
    def pre_save_receiver(sender, instance, *args, **kwargs):
        if not instance.slug and instance.titel:
            instance.slug = slugify(instance.titel.rsplit(None, 1)[1])


class Dokumente(models.Model):
    id = models.AutoField(primary_key=True)
    slug = models.TextField()
    titel = models.TextField()
    jahr = models.IntegerField()
    text_de = models.TextField()
    text_eng = models.TextField()
    img = models.TextField()
    denker = models.TextField()
    orte = models.TextField()
    link = models.TextField()
    autor = models.TextField()

    class Meta:
        managed = True
        db_table = 'dokumente'
        verbose_name = 'Dokument'
        verbose_name_plural = 'Dokumente'
