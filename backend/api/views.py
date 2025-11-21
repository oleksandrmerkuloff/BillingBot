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
        serializer = MeterSerializer(meter)
        return Response(serializer.data)

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


class ReportViewSet(ViewSet):
    def list(self, request):
        queryset = Report.objects.all()
        serializer = ReportSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ReportSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def retrieve(self, request, pk=None):
        report = get_object_or_404(Report, pk=pk)
        serializer = ReportSerializer(report)
        return Response(serializer.data)

    def update(self, request, pk=None):
        report = get_object_or_404(Report, pk=pk)
        serializer = ReportSerializer(
            instance=report,
            data=request.data,
            )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def partial_update(self, request, pk=None):
        report = get_object_or_404(Report, pk=pk)
        serializer = ReportSerializer(
            instance=report,
            data=request.data,
            partial=True
            )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def destroy(self, request, pk=None):
        report = get_object_or_404(Report, pk=pk)
        report.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
