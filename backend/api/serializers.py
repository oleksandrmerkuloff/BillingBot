from rest_framework import serializers

from api.models import Report, ReportItem, Meter


class ReportItemSerializer(serializers.ModelSerializer):
    total = serializers.ReadOnlyField()

    class Meta:
        model = ReportItem
        fields = [
            'id',
            'meter',
            'report',
            'consume',
            'created_at',
            'total'
            ]


class ReportSerializer(serializers.ModelSerializer):
    items = ReportItemSerializer(many=True, read_only=True)
    is_paid = serializers.ReadOnlyField()
    total = serializers.ReadOnlyField()

    class Meta:
        model = Report
        fields = [
            'id',
            'items',
            'created_at',
            'bill',
            'is_paid',
            'total'
            ]


class MeterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meter
        fields = [
            'id',
            'name',
            'meter_number',
            'price_per_unit',
            'unit_name',
            'total_consumed',
            'updated_at'
        ]
