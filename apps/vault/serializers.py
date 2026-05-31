from rest_framework import serializers

from .models import VaultDocument


class VaultDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = VaultDocument
        fields = "__all__"
