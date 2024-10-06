from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(WorkshopStatus)
class WorkshopStatusAdmin(admin.ModelAdmin):
    list_display = ('status_code', 'status_title')


@admin.register(Workshop)
class WorkshopAdmin(admin.ModelAdmin):
    list_display = ('title', 'place', 'teacher', 'view_number', 'register_date', 'is_active',)


@admin.register(WorkshopGallery)
class WorkshopGalleryAdmin(admin.ModelAdmin):
    list_display = ('workshop',)