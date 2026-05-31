from django.contrib import admin

from .models import Expense, ExpensePhoto, ExpenseReceipt


class ExpensePhotoInline(admin.TabularInline):
    model = ExpensePhoto
    extra = 0


class ExpenseReceiptInline(admin.TabularInline):
    model = ExpenseReceipt
    extra = 0


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ("date", "property", "category", "amount", "vendor", "is_tax_deductible")
    list_filter = ("category", "is_tax_deductible")
    search_fields = ("property__name", "vendor", "description")
    autocomplete_fields = ("property",)
    inlines = [ExpensePhotoInline, ExpenseReceiptInline]


@admin.register(ExpensePhoto)
class ExpensePhotoAdmin(admin.ModelAdmin):
    list_display = ("expense", "caption")


@admin.register(ExpenseReceipt)
class ExpenseReceiptAdmin(admin.ModelAdmin):
    list_display = ("expense", "title")
