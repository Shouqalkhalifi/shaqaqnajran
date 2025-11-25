from django.contrib import admin

from .models import Unit


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ("name", "owner", "city", "price_per_night", "is_active")
    list_filter = ("city", "is_active")
    search_fields = ("name", "address", "owner__username")
