from django.db import models
from django.utils.text import slugify


class Orte(models.Model):
    id = models.AutoField(primary_key=True)
    slug = models.SlugField(allow_unicode=True, unique=True, max_length=250, null=True, blank=True)
    name = models.CharField(max_length=250)
    img = models.CharField(max_length=500)
    text = models.TextField()
    text_en = models.TextField()
    lat = models.FloatField()
    lng = models.FloatField()
    denker_slugs = models.CharField(max_length=500)
    denker = models.ManyToManyField('denker.Denker')

    def __str__(self):
        return (str(self.id) + " | " + str(self.name))

    class Meta:
        managed = True
        db_table = 'orte'
        verbose_name = 'Ort'
        verbose_name_plural = 'Orte'

    def pre_save_receiver(sender, instance, *args, **kwargs):
        if not instance.slug and instance.titel:
            instance.slug = slugify(instance.name.rsplit(None, 1)[1])
