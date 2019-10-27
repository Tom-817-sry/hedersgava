from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __unicode__(self):
        # 在Python3中使用 def __str__(self):
        return self.name


class Meizis(models.Model):
    mid = models.CharField(max_length=10)
    title = models.CharField(max_length=50, blank=True, null=True)
    picname = models.CharField(max_length=10, blank=True, null=True)
    page_url = models.CharField(max_length=50, blank=True, null=True)
    img_url = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meizi_meizis'