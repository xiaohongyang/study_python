from django.contrib import admin
from .models import Person

# Register your models here.



class PersonAdmin(admin.ModelAdmin):
    list_display = ('id','title','pub_date',)
    search_fields = ('title', 'id')

    def get_search_results(self, request, queryset, search_term):
        queryset, use_distinct = super(PersonAdmin, self).get_search_results(request, queryset, search_term)

        try:
            search_id = int(search_term)
            queryset = self.model.objects.filter(pub_date__contains=search_id)
        except Exception as err:
            pass

        return  queryset, use_distinct;

admin.site.register(Person, PersonAdmin)