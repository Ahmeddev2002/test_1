from rest_framework import viewsets

from .models import Lease
from .serializers import LeaseSerializer


class LeaseViewSet(viewsets.ModelViewSet):
    queryset = Lease.objects.select_related("property", "tenant").all()
    serializer_class = LeaseSerializer
    filterset_fields = ["property", "tenant", "is_active"]
    ordering_fields = ["start_date", "end_date", "monthly_rent"]
