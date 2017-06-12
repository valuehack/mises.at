from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify


class Denker(models.Model):
    id = models.AutoField(primary_key=True)
    slug = models.CharField(max_length=250, unique=True, null=True, blank=True)
    name = models.CharField(max_length=250)
    img = models.CharField(max_length=250)
    bio = models.TextField()
    bio_en = models.TextField(null=True, blank=True)
    geburt = models.DateField(null=True, blank=True)
    tod = models.DateField(null=True, blank=True)
    gen = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'denker'
        verbose_name = 'Denker'
        verbose_name_plural = 'Denker'

    def __str__(self):
        return self.name
        

def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug and instance.name:
        instance.slug = slugify(instance.name.rsplit(None, 1)[1])


pre_save.connect(pre_save_receiver, sender=Denker)
