from django.contrib import admin

from .models import Tenant, TenantDocument


class TenantDocumentInline(admin.TabularInline):
    model = TenantDocument
    extra = 0


@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ("name", "cnic", "phone")
    search_fields = ("name", "cnic", "phone")
    inlines = [TenantDocumentInline]


@admin.register(TenantDocument)
class TenantDocumentAdmin(admin.ModelAdmin):
    list_display = ("tenant", "title", "doc_type")
    list_filter = ("doc_type",)
    search_fields = ("tenant__name", "title")
