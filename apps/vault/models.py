from __future__ import annotations

from django.db import models

from apps.common import TimestampedModel


class VaultDocument(TimestampedModel):
    class DocType(models.TextChoices):
        FBR_NOTICE = "fbr_notice", "FBR Notice"
        CANTONMENT_NOTICE = "cantonment_notice", "Cantonment Board Notice"
        SECTION_7E = "section_7e", "Section 7E Exemption Certificate"
        NADRA = "nadra", "NADRA Document"
        CORRESPONDENCE = "correspondence", "Correspondence"
        OTHER = "other", "Other"

    title = models.CharField(max_length=200)
    doc_type = models.CharField(max_length=30, choices=DocType.choices)
    property = models.ForeignKey(
        "properties.Property",
        related_name="vault_documents",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    file = models.FileField(upload_to="vault/")
    issued_on = models.DateField(null=True, blank=True)
    reference = models.CharField(max_length=120, blank=True)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["-issued_on", "-created_at"]

    def __str__(self) -> str:
        return self.title
