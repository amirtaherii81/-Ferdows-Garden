from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Place)
class PlaceAmdmin(admin.ModelAdmin):
    list_display = ('place_name', 'place_image_name', 'visiting_day', 'visiting_hour', 'register_date')


@admin.register(VisitorType)
class VisitorTypeAmdmin(admin.ModelAdmin):
    list_display = ('type_name',)


@admin.register(TicketPrice)
class TicketPriceAmdmin(admin.ModelAdmin):
    list_display = ('place', 'visitor_type', 'price')

@admin.register(Message)
class MessageAmdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'subject', 'is_seen', 'register_date',)