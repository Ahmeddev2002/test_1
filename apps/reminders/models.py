from __future__ import annotations

from django.db import models

from apps.common import TimestampedModel


class Reminder(TimestampedModel):
    class Type(models.TextChoices):
        LEASE_EXPIRY = "lease_expiry", "Lease Expiry"
        RENT_DUE = "rent_due", "Rent Due"
        PROPERTY_TAX = "property_tax", "Property Tax Filing"
        INSURANCE = "insurance", "Insurance Renewal"
        CUSTOM = "custom", "Custom"

    title = models.CharField(max_length=200)
    reminder_type = models.CharField(max_length=20, choices=Type.choices)
    trigger_date = models.DateField()
    property = models.ForeignKey(
        "properties.Property",
        related_name="reminders",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    lease = models.ForeignKey(
        "leases.Lease",
        related_name="reminders",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    is_sent = models.BooleanField(default=False)
    sent_at = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["trigger_date"]

    def __str__(self) -> str:
        return f"{self.get_reminder_type_display()}: {self.title} ({self.trigger_date})"
