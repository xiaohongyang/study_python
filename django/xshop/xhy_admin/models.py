from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible
class Article(models.Model):
    title = models.CharField(u'标题',max_length=255)
    content = models.TextField(u'内容')
    pub_date = models.DateTimeField(u'发布时间',auto_now_add=True,editable=True)
    update_time = models.DateTimeField(u'更新时间',auto_now=True,null=True)
    user = models.ForeignKey('auth.User',blank=True,null=True, verbose_name='作者')

    def __str__(self):
        return  self.title

    def mycontent(self):
        return  self.content
    mycontent.short_description = "详情"

    thecontent = property(mycontent)

