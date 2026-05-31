from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.communications.views import CommunicationAttachmentViewSet, CommunicationLogViewSet
from apps.expenses.views import ExpensePhotoViewSet, ExpenseReceiptViewSet, ExpenseViewSet
from apps.leases.views import LeaseViewSet
from apps.payments.views import RentInvoiceViewSet, RentPaymentViewSet, WithholdingTaxViewSet
from apps.properties.views import PropertyDocumentViewSet, PropertyPhotoViewSet, PropertyViewSet
from apps.reminders.views import ReminderViewSet
from apps.taxes.views import TaxYearSummaryView
from apps.tenants.views import TenantDocumentViewSet, TenantViewSet
from apps.vault.views import VaultDocumentViewSet

router = DefaultRouter()
router.register("properties", PropertyViewSet)
router.register("property-photos", PropertyPhotoViewSet)
router.register("property-documents", PropertyDocumentViewSet)
router.register("tenants", TenantViewSet)
router.register("tenant-documents", TenantDocumentViewSet)
router.register("leases", LeaseViewSet)
router.register("rent-invoices", RentInvoiceViewSet)
router.register("rent-payments", RentPaymentViewSet)
router.register("withholding-tax", WithholdingTaxViewSet)
router.register("expenses", ExpenseViewSet)
router.register("expense-photos", ExpensePhotoViewSet)
router.register("expense-receipts", ExpenseReceiptViewSet)
router.register("communications", CommunicationLogViewSet)
router.register("communication-attachments", CommunicationAttachmentViewSet)
router.register("vault-documents", VaultDocumentViewSet)
router.register("reminders", ReminderViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(router.urls)),
    path("api/v1/tax-years/<int:year>/", TaxYearSummaryView.as_view(), name="tax-year-summary"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
