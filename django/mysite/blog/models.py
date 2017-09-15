from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100,default='')
    content = models.TextField(blank=True)

    def __str__(self):
        return self.title
    def __unicode__(self):
        return  self.title




