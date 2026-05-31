from __future__ import annotations

from django.db import models

from apps.common import TimestampedModel


class CommunicationLog(TimestampedModel):
    class Type(models.TextChoices):
        COMPLAINT = "complaint", "Complaint"
        REQUEST = "request", "Request"
        REPAIR = "repair", "Repair Needed"
        NOTICE = "notice", "Notice"
        OTHER = "other", "Other"

    class Status(models.TextChoices):
        OPEN = "open", "Open"
        IN_PROGRESS = "in_progress", "In Progress"
        RESOLVED = "resolved", "Resolved"
        CLOSED = "closed", "Closed"

    property = models.ForeignKey(
        "properties.Property", related_name="communications", on_delete=models.CASCADE
    )
    tenant = models.ForeignKey(
        "tenants.Tenant",
        related_name="communications",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    occurred_on = models.DateField()
    log_type = models.CharField(max_length=20, choices=Type.choices)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.OPEN)
    description = models.TextField()
    response = models.TextField(blank=True)
    resolved_on = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ["-occurred_on", "-created_at"]

    def __str__(self) -> str:
        return f"{self.get_log_type_display()} — {self.property.name} ({self.occurred_on})"


class CommunicationAttachment(TimestampedModel):
    log = models.ForeignKey(
        CommunicationLog, related_name="attachments", on_delete=models.CASCADE
    )
    file = models.FileField(upload_to="communications/")
    caption = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ["-created_at"]
