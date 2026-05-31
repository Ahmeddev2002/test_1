from __future__ import annotations

from django.db import models

from apps.common import TimestampedModel


class Expense(TimestampedModel):
    class Category(models.TextChoices):
        REPAIR = "repair", "Repair"
        MAINTENANCE = "maintenance", "Maintenance"
        PROPERTY_TAX = "property_tax", "Property Tax"
        CANTONMENT_DUES = "cantonment_dues", "Cantonment/Society Dues"
        INSURANCE = "insurance", "Insurance Premium"
        UTILITY = "utility", "Utility Bill"
        LEGAL = "legal", "Legal / Professional"
        OTHER = "other", "Other"

    property = models.ForeignKey(
        "properties.Property",
        related_name="expenses",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        help_text="Leave blank for portfolio-level expenses.",
    )
    date = models.DateField()
    category = models.CharField(max_length=20, choices=Category.choices)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    vendor = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    is_tax_deductible = models.BooleanField(default=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self) -> str:
        target = self.property.name if self.property else "Portfolio"
        return f"{self.get_category_display()} — {self.amount} ({target}, {self.date})"


class ExpensePhoto(TimestampedModel):
    expense = models.ForeignKey(Expense, related_name="photos", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="expenses/photos/")
    caption = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ["-created_at"]


class ExpenseReceipt(TimestampedModel):
    expense = models.ForeignKey(Expense, related_name="receipts", on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True)
    file = models.FileField(upload_to="expenses/receipts/")

    class Meta:
        ordering = ["-created_at"]
