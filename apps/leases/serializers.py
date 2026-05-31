from rest_framework import serializers

from .models import Lease


class LeaseSerializer(serializers.ModelSerializer):
    property_name = serializers.CharField(source="property.name", read_only=True)
    tenant_name = serializers.CharField(source="tenant.name", read_only=True)

    class Meta:
        model = Lease
        fields = "__all__"
