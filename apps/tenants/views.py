from rest_framework import viewsets

from .models import Tenant, TenantDocument
from .serializers import TenantDocumentSerializer, TenantSerializer


class TenantViewSet(viewsets.ModelViewSet):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    search_fields = ["name", "cnic", "phone"]
    ordering_fields = ["name", "created_at"]


class TenantDocumentViewSet(viewsets.ModelViewSet):
    queryset = TenantDocument.objects.all()
    serializer_class = TenantDocumentSerializer
    filterset_fields = ["tenant", "doc_type"]
