from rest_framework import viewsets

from .models import Reminder
from .serializers import ReminderSerializer


class ReminderViewSet(viewsets.ModelViewSet):
    queryset = Reminder.objects.select_related("property", "lease").all()
    serializer_class = ReminderSerializer
    filterset_fields = ["reminder_type", "is_sent", "property", "lease"]
    ordering_fields = ["trigger_date"]
