from django.contrib import admin
from .models import Event, Booking

# Register your models here.
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    pass
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['name' ,'date' , 'total_seats' , 'available_seats']