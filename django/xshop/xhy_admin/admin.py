'''
后台配置
'''
from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date','update_time','thecontent')
    search_fields = ['title','content']
    list_filter = ('title', 'update_time')
    fieldsets = [
        ('group1', {'fields': ['title']}),
        ('group2', {'fields' : ['content']})
    ]

    #搜索过滤
    def get_queryset(self, request):
        qs = super(ArticleAdmin,self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            rs = qs.filter(user=request.user)
            return  rs


    #搜索定制
    def get_search_results(self, request, queryset, search_term):
        queryset,use_distinct = super(ArticleAdmin,self).get_search_results(request, queryset, search_term)

        try:
            search_term_value = str(search_term)
            pass
        except ValueError:
            pass
        else:
            myfilter = self.model.objects.filter(content__regex=""+search_term_value)
            myfilter |= self.model.objects.filter(title__regex=""+search_term_value+"$")
            queryset &= myfilter

        return  queryset, use_distinct

    #保存
    def save_model(self, request, obj, form, change):
        if request.user.is_superuser == False and obj.user == None:
            obj.user = request.user
        obj.save()
        #super().save_model(request, obj, form, change)
# Register your models here.
admin.site.register(Article, ArticleAdmin)

