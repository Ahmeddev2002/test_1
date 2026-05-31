from django.contrib import admin

from .models import CommunicationAttachment, CommunicationLog


class CommunicationAttachmentInline(admin.TabularInline):
    model = CommunicationAttachment
    extra = 0


@admin.register(CommunicationLog)
class CommunicationLogAdmin(admin.ModelAdmin):
    list_display = ("occurred_on", "property", "tenant", "log_type", "status", "resolved_on")
    list_filter = ("log_type", "status")
    search_fields = ("property__name", "tenant__name", "description")
    autocomplete_fields = ("property", "tenant")
    inlines = [CommunicationAttachmentInline]


@admin.register(CommunicationAttachment)
class CommunicationAttachmentAdmin(admin.ModelAdmin):
    list_display = ("log", "caption")
