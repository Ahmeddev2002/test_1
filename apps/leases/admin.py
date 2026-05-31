from django.contrib import admin

from .models import Lease


@admin.register(Lease)
class LeaseAdmin(admin.ModelAdmin):
    list_display = (
        "property",
        "tenant",
        "start_date",
        "end_date",
        "monthly_rent",
        "annual_escalation_pct",
        "is_active",
    )
    list_filter = ("is_active",)
    search_fields = ("property__name", "tenant__name")
    autocomplete_fields = ("property", "tenant")
