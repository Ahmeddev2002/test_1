from rest_framework import viewsets

from .models import Expense, ExpensePhoto, ExpenseReceipt
from .serializers import ExpensePhotoSerializer, ExpenseReceiptSerializer, ExpenseSerializer


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.select_related("property").all()
    serializer_class = ExpenseSerializer
    filterset_fields = ["property", "category", "is_tax_deductible"]
    search_fields = ["vendor", "description", "property__name"]
    ordering_fields = ["date", "amount"]


class ExpensePhotoViewSet(viewsets.ModelViewSet):
    queryset = ExpensePhoto.objects.all()
    serializer_class = ExpensePhotoSerializer
    filterset_fields = ["expense"]


class ExpenseReceiptViewSet(viewsets.ModelViewSet):
    queryset = ExpenseReceipt.objects.all()
    serializer_class = ExpenseReceiptSerializer
    filterset_fields = ["expense"]
