from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(default='')

    def __str__(self):
        return self.title

class WorkTime(models.Model):
    id = models.AutoField(primary_key=True)
    oa_id = models.IntegerField()
    clocktime = models.DateTimeField()