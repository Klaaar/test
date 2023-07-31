from django.contrib import admin
from .models import Advertisements
# Register your models here.
#регистрируем модель
class AdvertisementsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'created_at','auction', 'updated_at']

admin.site.register(Advertisements, AdvertisementsAdmin)
