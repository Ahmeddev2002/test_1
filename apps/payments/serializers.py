from rest_framework import serializers

from .models import RentInvoice, RentPayment, WithholdingTax


class RentPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentPayment
        fields = "__all__"


class WithholdingTaxSerializer(serializers.ModelSerializer):
    class Meta:
        model = WithholdingTax
        fields = "__all__"


class RentInvoiceSerializer(serializers.ModelSerializer):
    payments = RentPaymentSerializer(many=True, read_only=True)
    withholding_taxes = WithholdingTaxSerializer(many=True, read_only=True)
    amount_paid = serializers.DecimalField(max_digits=12, decimal_places=2, read_only=True)
    outstanding = serializers.DecimalField(max_digits=12, decimal_places=2, read_only=True)
    is_paid = serializers.BooleanField(read_only=True)

    class Meta:
        model = RentInvoice
        fields = "__all__"
