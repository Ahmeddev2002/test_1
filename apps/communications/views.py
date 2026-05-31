from rest_framework import viewsets

from .models import CommunicationAttachment, CommunicationLog
from .serializers import CommunicationAttachmentSerializer, CommunicationLogSerializer


class CommunicationLogViewSet(viewsets.ModelViewSet):
    queryset = CommunicationLog.objects.select_related("property", "tenant").all()
    serializer_class = CommunicationLogSerializer
    filterset_fields = ["property", "tenant", "log_type", "status"]
    search_fields = ["description", "response"]
    ordering_fields = ["occurred_on", "resolved_on"]


class CommunicationAttachmentViewSet(viewsets.ModelViewSet):
    queryset = CommunicationAttachment.objects.all()
    serializer_class = CommunicationAttachmentSerializer
    filterset_fields = ["log"]
