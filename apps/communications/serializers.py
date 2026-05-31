from rest_framework import serializers

from .models import CommunicationAttachment, CommunicationLog


class CommunicationAttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommunicationAttachment
        fields = "__all__"


class CommunicationLogSerializer(serializers.ModelSerializer):
    attachments = CommunicationAttachmentSerializer(many=True, read_only=True)

    class Meta:
        model = CommunicationLog
        fields = "__all__"
