from django.contrib import admin
from .models import BlogApp2

# Register your models here.
class BlogApp2Admin(admin.ModelAdmin):
    list_display = ('id','title')


admin.site.register(BlogApp2, BlogApp2Admin)