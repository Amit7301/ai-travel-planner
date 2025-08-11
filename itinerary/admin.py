from django.contrib import admin
from .models import Itinerary

@admin.register(Itinerary)
class ItineraryAdmin(admin.ModelAdmin):
    list_display = ['source', 'destination', 'days', 'budget', 'travel_style', 'created_at']
    list_filter = ['budget', 'travel_style', 'days', 'created_at']
    search_fields = ['source', 'destination']
    readonly_fields = ['created_at']