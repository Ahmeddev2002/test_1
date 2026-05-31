from django.contrib import admin

from .models import Reminder


@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ("trigger_date", "reminder_type", "title", "property", "lease", "is_sent")
    list_filter = ("reminder_type", "is_sent")
    search_fields = ("title", "notes")
    autocomplete_fields = ("property", "lease")
