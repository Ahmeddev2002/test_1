from __future__ import annotations

from django.core.validators import RegexValidator
from django.db import models

from apps.common import TimestampedModel

CNIC_VALIDATOR = RegexValidator(
    regex=r"^\d{5}-\d{7}-\d$",
    message="CNIC must be in the format XXXXX-XXXXXXX-X.",
)


class Tenant(TimestampedModel):
    name = models.CharField(max_length=200)
    cnic = models.CharField(max_length=15, unique=True, validators=[CNIC_VALIDATOR])
    phone = models.CharField(max_length=20)
    emergency_contact_name = models.CharField(max_length=200, blank=True)
    emergency_contact_phone = models.CharField(max_length=20, blank=True)
    photo = models.ImageField(upload_to="tenants/photos/", null=True, blank=True)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class TenantDocument(TimestampedModel):
    class DocType(models.TextChoices):
        CNIC = "cnic", "CNIC Copy"
        LEASE = "lease", "Lease Agreement"
        REFERENCE = "reference", "Reference"
        OTHER = "other", "Other"

    tenant = models.ForeignKey(Tenant, related_name="documents", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    doc_type = models.CharField(max_length=20, choices=DocType.choices)
    file = models.FileField(upload_to="tenants/documents/")
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.tenant.name} — {self.title}"
