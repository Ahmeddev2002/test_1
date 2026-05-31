from django.contrib import admin

from .models import RentInvoice, RentPayment, WithholdingTax


class RentPaymentInline(admin.TabularInline):
    model = RentPayment
    extra = 0


class WithholdingTaxInline(admin.TabularInline):
    model = WithholdingTax
    extra = 0


@admin.register(RentInvoice)
class RentInvoiceAdmin(admin.ModelAdmin):
    list_display = ("lease", "period_start", "period_end", "due_date", "amount_due", "is_paid")
    list_filter = ("due_date",)
    search_fields = ("lease__property__name", "lease__tenant__name")
    autocomplete_fields = ("lease",)
    inlines = [RentPaymentInline, WithholdingTaxInline]


@admin.register(RentPayment)
class RentPaymentAdmin(admin.ModelAdmin):
    list_display = ("invoice", "paid_on", "amount", "method", "reference")
    list_filter = ("method", "paid_on")
    search_fields = ("invoice__lease__tenant__name", "reference")


@admin.register(WithholdingTax)
class WithholdingTaxAdmin(admin.ModelAdmin):
    list_display = ("invoice", "deducted_on", "amount", "certificate_ref")
    search_fields = ("invoice__lease__tenant__name", "certificate_ref")
