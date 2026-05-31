from rest_framework import viewsets

from .models import RentInvoice, RentPayment, WithholdingTax
from .serializers import RentInvoiceSerializer, RentPaymentSerializer, WithholdingTaxSerializer


class RentInvoiceViewSet(viewsets.ModelViewSet):
    queryset = RentInvoice.objects.select_related(
        "lease__property", "lease__tenant"
    ).prefetch_related("payments", "withholding_taxes")
    serializer_class = RentInvoiceSerializer
    filterset_fields = ["lease", "lease__property", "lease__tenant"]
    ordering_fields = ["period_start", "due_date"]


class RentPaymentViewSet(viewsets.ModelViewSet):
    queryset = RentPayment.objects.select_related("invoice").all()
    serializer_class = RentPaymentSerializer
    filterset_fields = ["invoice", "method"]
    ordering_fields = ["paid_on", "amount"]


class WithholdingTaxViewSet(viewsets.ModelViewSet):
    queryset = WithholdingTax.objects.select_related("invoice").all()
    serializer_class = WithholdingTaxSerializer
    filterset_fields = ["invoice"]
