from django.contrib import admin

from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("unit", "tenant", "start_date", "end_date", "status", "created_at")
    list_filter = ("status", "start_date", "end_date")
    search_fields = ("unit__name", "tenant__username")
