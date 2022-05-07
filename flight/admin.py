from django.contrib import admin
from .models import *


class CityAdmin(admin.ModelAdmin):
    list_display = ['id', "country_name", 'city_name', 'city_code']


class AirportAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'city_code', 'terminal', 'gate']


class AirplaneAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'number_of_seats']


class FlightAdmin(admin.ModelAdmin):
    list_display = ["id", 'source', 'destination', 'airplane', 'cost', 'flight_type', 'departure_date']
    list_filter = ('departure_date',)


class TicketAdmin(admin.ModelAdmin):
    list_display = ["id", "ticket_code", "flight"]


# Register your models here.
admin.site.register(City, CityAdmin)
admin.site.register(Airport, AirportAdmin)
admin.site.register(Airplane, AirplaneAdmin)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Ticket, TicketAdmin)
