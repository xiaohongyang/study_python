from django.db import models

# Create your models here.

class Article(models.Model):
    arc_id = models.IntegerField(blank=False,default=0)
    title = models.CharField(max_length=255,blank=False,default='')
    content = models.TextField(blank=False,default='')