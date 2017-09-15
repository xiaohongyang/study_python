import ast


from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    sex = models.SmallIntegerField()

    def __unicode__(self):
        return  self.name

    def __str__(self):
        return self.name


#自定义字段
class ListField(models.TextField):
    __metaclass__ = models.SubfieldBase
    description = "Store a python list"

    def __init__(self, *args, **kwargs):
        super(ListField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value:
            value = []
        if isinstance(value, list):
            return  value
        return  ast.literal_eval(value);

    def get_prep_value(self, value):
        if value is None:
            return  value
        return str(value)

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return  self.get_db_prep_value(value)

class Article(models.Model):
    labels = ListField()

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return  self.name

class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ForeignKey(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):

        return self.headline