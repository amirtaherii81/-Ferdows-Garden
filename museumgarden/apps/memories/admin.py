from django.contrib import admin
from .models import Memory
# Register your models here.

@admin.register(Memory)
class MemoryAdmin(admin.ModelAdmin):
    list_display = ('memory_title', 'register_date', 'is_active', 'user_registered',)