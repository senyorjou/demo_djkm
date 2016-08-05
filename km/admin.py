from django.contrib import admin

from .models import Customer, Location, Product, Provider, Province


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    fields = ('name', 'website', 'location', 'products')
    list_display = ('name', 'website', 'location')


@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    fields = ('name', 'website', 'location')
    list_display = ('name', 'website', 'location')


@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    fields = ('zip_prefix', 'name')
    list_display = ('zip_prefix', 'name')


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    fields = ('name', 'zip_code')
    list_display = ('name', 'zip_code', 'province')
