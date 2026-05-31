from rest_framework import viewsets

from .models import Property, PropertyDocument, PropertyPhoto
from .serializers import PropertyDocumentSerializer, PropertyPhotoSerializer, PropertySerializer


class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    filterset_fields = ["property_type", "status"]
    search_fields = ["name", "address"]
    ordering_fields = ["name", "created_at"]


class PropertyPhotoViewSet(viewsets.ModelViewSet):
    queryset = PropertyPhoto.objects.all()
    serializer_class = PropertyPhotoSerializer
    filterset_fields = ["property", "category"]


class PropertyDocumentViewSet(viewsets.ModelViewSet):
    queryset = PropertyDocument.objects.all()
    serializer_class = PropertyDocumentSerializer
    filterset_fields = ["property", "doc_type"]
