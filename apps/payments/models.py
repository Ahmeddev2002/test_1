from __future__ import annotations

from decimal import Decimal

from django.db import models
from django.db.models import Sum

from apps.common import TimestampedModel


class RentInvoice(TimestampedModel):
    lease = models.ForeignKey(
        "leases.Lease", related_name="invoices", on_delete=models.CASCADE
    )
    period_start = models.DateField()
    period_end = models.DateField()
    due_date = models.DateField()
    amount_due = models.DecimalField(max_digits=12, decimal_places=2)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["-period_start"]
        constraints = [
            models.UniqueConstraint(
                fields=["lease", "period_start"], name="unique_invoice_per_lease_period"
            )
        ]

    def __str__(self) -> str:
        return f"Invoice {self.lease} {self.period_start:%b %Y}"

    @property
    def amount_paid(self) -> Decimal:
        return self.payments.aggregate(total=Sum("amount"))["total"] or Decimal("0")

    @property
    def outstanding(self) -> Decimal:
        return self.amount_due - self.amount_paid

    @property
    def is_paid(self) -> bool:
        return self.outstanding <= Decimal("0")


class RentPayment(TimestampedModel):
    class Method(models.TextChoices):
        CASH = "cash", "Cash"
        BANK_TRANSFER = "bank_transfer", "Bank Transfer"
        CHEQUE = "cheque", "Cheque"
        OTHER = "other", "Other"

    invoice = models.ForeignKey(
        RentInvoice, related_name="payments", on_delete=models.CASCADE
    )
    paid_on = models.DateField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    method = models.CharField(max_length=20, choices=Method.choices, default=Method.CASH)
    reference = models.CharField(max_length=120, blank=True, help_text="Cheque #, transaction ID, etc.")
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["-paid_on"]

    def __str__(self) -> str:
        return f"{self.amount} paid on {self.paid_on} for {self.invoice}"


class WithholdingTax(TimestampedModel):
    """WHT deducted by a corporate tenant on rent paid."""

    invoice = models.ForeignKey(
        RentInvoice, related_name="withholding_taxes", on_delete=models.CASCADE
    )
    deducted_on = models.DateField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    certificate_ref = models.CharField(max_length=120, blank=True)
    certificate_file = models.FileField(upload_to="payments/wht/", null=True, blank=True)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["-deducted_on"]
        verbose_name = "withholding tax entry"
        verbose_name_plural = "withholding tax entries"

    def __str__(self) -> str:
        return f"WHT {self.amount} on {self.invoice}"
