from django.contrib import admin
from . import models


class CategoryAdmin(admin.ModelAdmin):
    model = models.Category


class CityAdmin(admin.ModelAdmin):
    model = models.City
    
    
class AdvertAdmin(admin.ModelAdmin):
    model = models.Advert
    
    
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.City, CityAdmin)
admin.site.register(models.Advert, AdvertAdmin)