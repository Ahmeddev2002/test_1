from rest_framework import viewsets

from .models import VaultDocument
from .serializers import VaultDocumentSerializer


class VaultDocumentViewSet(viewsets.ModelViewSet):
    queryset = VaultDocument.objects.select_related("property").all()
    serializer_class = VaultDocumentSerializer
    filterset_fields = ["doc_type", "property"]
    search_fields = ["title", "reference", "notes"]
    ordering_fields = ["issued_on"]
