from django.contrib import admin

from .models import Location, Province


@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    fields = ('zip_prefix', 'name')
    list_display = ('zip_prefix', 'name')


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    fields = ('name', 'zip_code')
    list_display = ('name', 'zip_code', 'province')
