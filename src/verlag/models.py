from django.db import models


class Verlagsprogramm(models.Model):
    id = models.AutoField(primary_key=True)
    slug = models.TextField()
    title = models.TextField()
    desc = models.TextField()
    author = models.TextField(null=True, blank=True)
    link = models.TextField()
    denker = models.ManyToManyField('denker.Denker', blank=True)

    def __str__(self):
        return (str(self.id) + " | " + str(self.title))

    class Meta:
        managed = True
        db_table = 'verlagsprogramm'
