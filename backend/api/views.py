from rest_framework.viewsets import ModelViewSet

from api.models import Meter, Report
from api.serializers import MeterSerializer, ReportSerializer


class MeterViewSet(ModelViewSet):
    queryset = Meter.objects.all()
    serializer_class = MeterSerializer


class ReportViewSet(ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
