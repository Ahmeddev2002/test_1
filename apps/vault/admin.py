from django.contrib import admin

from .models import VaultDocument


@admin.register(VaultDocument)
class VaultDocumentAdmin(admin.ModelAdmin):
    list_display = ("title", "doc_type", "property", "issued_on", "reference")
    list_filter = ("doc_type",)
    search_fields = ("title", "reference", "notes")
    autocomplete_fields = ("property",)
