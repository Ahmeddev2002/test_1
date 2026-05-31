from __future__ import annotations

from django.db import models

from apps.common import TimestampedModel


class Property(TimestampedModel):
    class Type(models.TextChoices):
        HOUSE = "house", "House"
        APARTMENT = "apartment", "Apartment"
        PLOT = "plot", "Plot"

    class AreaUnit(models.TextChoices):
        MARLA = "marla", "Marla"
        KANAL = "kanal", "Kanal"
        SQ_FT = "sq_ft", "Square Feet"
        SQ_YD = "sq_yd", "Square Yards"

    class Status(models.TextChoices):
        RENTED = "rented", "Rented"
        VACANT = "vacant", "Vacant"
        UNDER_CONSTRUCTION = "under_construction", "Under Construction"
        FOR_SALE = "for_sale", "For Sale"

    name = models.CharField(max_length=200)
    address = models.TextField()
    property_type = models.CharField(max_length=20, choices=Type.choices)
    area_value = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    area_unit = models.CharField(max_length=10, choices=AreaUnit.choices, default=AreaUnit.MARLA)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.VACANT)
    notes = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "properties"
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class PropertyPhoto(TimestampedModel):
    class Category(models.TextChoices):
        PRE_TENANT = "pre_tenant", "Pre-tenant condition"
        CURRENT = "current", "Current state"
        DAMAGE = "damage", "Damage record"
        OTHER = "other", "Other"

    property = models.ForeignKey(Property, related_name="photos", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="properties/photos/")
    taken_on = models.DateField()
    category = models.CharField(max_length=20, choices=Category.choices, default=Category.CURRENT)
    caption = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ["-taken_on", "-created_at"]

    def __str__(self) -> str:
        return f"{self.property.name} — {self.get_category_display()} ({self.taken_on})"


class PropertyDocument(TimestampedModel):
    class DocType(models.TextChoices):
        REGISTRY = "registry", "Registry"
        TAX_RECEIPT = "tax_receipt", "Tax Receipt"
        UTILITY = "utility", "Utility Connection"
        OTHER = "other", "Other"

    property = models.ForeignKey(Property, related_name="documents", on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    doc_type = models.CharField(max_length=20, choices=DocType.choices)
    file = models.FileField(upload_to="properties/documents/")
    issued_on = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["-issued_on", "-created_at"]

    def __str__(self) -> str:
        return f"{self.property.name} — {self.title}"
