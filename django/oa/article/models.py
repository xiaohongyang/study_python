from django.db import models

# Create your models here.
class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255, default='')
    pub_date = models.DateTimeField('发布时间', auto_created=True, editable=True)

    def __unicode__(self):
        return  self.title

    def __str__(self):
        return self.title;

