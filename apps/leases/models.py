from __future__ import annotations

from decimal import Decimal

from django.conf import settings
from django.db import models
from django.db.models import Q

from apps.common import TimestampedModel


class Lease(TimestampedModel):
    property = models.ForeignKey(
        "properties.Property", related_name="leases", on_delete=models.PROTECT
    )
    tenant = models.ForeignKey(
        "tenants.Tenant", related_name="leases", on_delete=models.PROTECT
    )
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    monthly_rent = models.DecimalField(max_digits=12, decimal_places=2)
    security_deposit = models.DecimalField(
        max_digits=12, decimal_places=2, default=Decimal("0")
    )
    annual_escalation_pct = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=Decimal(str(settings.DEFAULT_ANNUAL_ESCALATION_PCT)),
        help_text="Percentage applied each anniversary year (Pakistani norm is ~10%).",
    )
    rent_due_day = models.PositiveSmallIntegerField(
        default=1, help_text="Day of month rent is due (1-28)."
    )
    is_active = models.BooleanField(default=True)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["-start_date"]
        constraints = [
            models.UniqueConstraint(
                fields=["property"],
                condition=Q(is_active=True),
                name="unique_active_lease_per_property",
            ),
        ]

    def __str__(self) -> str:
        return f"{self.tenant.name} @ {self.property.name} (from {self.start_date})"

    def rent_for_period(self, period_start) -> Decimal:
        """Compute monthly rent for a given period, applying annual escalation."""
        years_elapsed = (period_start.year - self.start_date.year) - (
            1 if (period_start.month, period_start.day) < (self.start_date.month, self.start_date.day) else 0
        )
        if years_elapsed <= 0:
            return self.monthly_rent
        multiplier = (Decimal("1") + self.annual_escalation_pct / Decimal("100")) ** years_elapsed
        return (self.monthly_rent * multiplier).quantize(Decimal("0.01"))
