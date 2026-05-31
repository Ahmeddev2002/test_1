from rest_framework import serializers

from .models import Tenant, TenantDocument


class TenantDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = TenantDocument
        fields = "__all__"


class TenantSerializer(serializers.ModelSerializer):
    documents = TenantDocumentSerializer(many=True, read_only=True)

    class Meta:
        model = Tenant
        fields = "__all__"
