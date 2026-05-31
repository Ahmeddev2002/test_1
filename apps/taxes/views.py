from __future__ import annotations

from decimal import Decimal

from django.db.models import Sum
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.expenses.models import Expense
from apps.payments.models import RentPayment, WithholdingTax

from .utils import tax_year_bounds


class TaxYearSummaryView(APIView):
    """Aggregate income/expense/WHT totals for a Pakistani tax year (Jul-Jun)."""

    def get(self, request, year: int):
        start, end = tax_year_bounds(year)

        rent_collected = RentPayment.objects.filter(
            paid_on__gte=start, paid_on__lte=end
        ).aggregate(total=Sum("amount"))["total"] or Decimal("0")

        wht_credited = WithholdingTax.objects.filter(
            deducted_on__gte=start, deducted_on__lte=end
        ).aggregate(total=Sum("amount"))["total"] or Decimal("0")

        deductible_expenses = Expense.objects.filter(
            date__gte=start, date__lte=end, is_tax_deductible=True
        ).aggregate(total=Sum("amount"))["total"] or Decimal("0")

        all_expenses = Expense.objects.filter(date__gte=start, date__lte=end).aggregate(
            total=Sum("amount")
        )["total"] or Decimal("0")

        net_taxable = rent_collected - deductible_expenses

        return Response(
            {
                "tax_year": year,
                "period": {"start": start, "end": end},
                "rent_collected": rent_collected,
                "withholding_tax_credit": wht_credited,
                "deductible_expenses": deductible_expenses,
                "all_expenses": all_expenses,
                "net_taxable_rental_income": net_taxable,
            }
        )
