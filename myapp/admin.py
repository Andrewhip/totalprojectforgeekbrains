from django.contrib import admin
from .models import News, Baraholka

admin.site.register(News)

class BaraholkaAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

admin.site.register(Baraholka, BaraholkaAdmin)