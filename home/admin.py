from django.contrib import admin
from .models import *

class ContactAdmin(admin.ModelAdmin):
    list_display=['name','phone','created_time']
    date_hierarchy = 'created_time'
    search_fields = ['name','message']

admin.site.register(Contact,ContactAdmin)