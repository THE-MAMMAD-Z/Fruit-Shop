from django.contrib import admin
from .models import *

class FruitAdmin(admin.ModelAdmin):
    list_display=['name','category','Capacity','available']
    date_hierarchy = 'created_time'
    search_fields = ['name','description']
    list_filter = ['category']

admin.site.register(Fruit,FruitAdmin)