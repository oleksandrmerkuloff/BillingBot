from rest_framework.viewsets import ViewSet
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

from api.models import Meter, Report
from api.serializers import MeterSerializer, ReportSerializer


class MeterViewSet(ViewSet):
    def list(self, request):
        queryset = Meter.objects.all()
        serializer = MeterSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = MeterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def retrieve(self, request, pk=None):
        meter = get_object_or_404(Meter, pk=pk)
        seralizer = MeterSerializer(meter)
        return Response(seralizer.data)

    def update(self, request, pk=None):
        meter = get_object_or_404(Meter, pk=pk)
        serializer = MeterSerializer(
            instance=meter,
            data=request.data,
            )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def partial_update(self, request, pk=None):
        meter = get_object_or_404(Meter, pk=pk)
        serializer = MeterSerializer(
            instance=meter,
            data=request.data,
            partial=True
            )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def destroy(self, request, pk=None):
        meter = get_object_or_404(Meter, pk=pk)
        meter.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ReportViewSet(ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
