from rest_framework import serializers

from .models import Expense, ExpensePhoto, ExpenseReceipt


class ExpensePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpensePhoto
        fields = "__all__"


class ExpenseReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseReceipt
        fields = "__all__"


class ExpenseSerializer(serializers.ModelSerializer):
    photos = ExpensePhotoSerializer(many=True, read_only=True)
    receipts = ExpenseReceiptSerializer(many=True, read_only=True)

    class Meta:
        model = Expense
        fields = "__all__"
