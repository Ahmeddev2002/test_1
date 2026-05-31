from django.contrib import admin

from .models import Property, PropertyDocument, PropertyPhoto


class PropertyPhotoInline(admin.TabularInline):
    model = PropertyPhoto
    extra = 0


class PropertyDocumentInline(admin.TabularInline):
    model = PropertyDocument
    extra = 0


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ("name", "property_type", "status", "area_value", "area_unit")
    list_filter = ("property_type", "status")
    search_fields = ("name", "address")
    inlines = [PropertyPhotoInline, PropertyDocumentInline]


@admin.register(PropertyPhoto)
class PropertyPhotoAdmin(admin.ModelAdmin):
    list_display = ("property", "category", "taken_on", "caption")
    list_filter = ("category",)
    search_fields = ("property__name", "caption")


@admin.register(PropertyDocument)
class PropertyDocumentAdmin(admin.ModelAdmin):
    list_display = ("property", "title", "doc_type", "issued_on")
    list_filter = ("doc_type",)
    search_fields = ("property__name", "title")
