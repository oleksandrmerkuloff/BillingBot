from django.contrib import admin

from api.models import Report, ReportItem, Meter


class ReportItemInline(admin.StackedInline):
    model = ReportItem


class MeterAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'meter_number',
        'price_per_unit',
        'unit_name',
        'total_consumed',
    )
    list_filter = (
        'updated_at'
    )
    search_fields = (
        'name',
    )


class ReportAdmin(admin.ModelAdmin):
    list_filter = (
        'is_paid',
    )
    inlines = [ReportItemInline]


admin.site.register(Meter, MeterAdmin)
admin.site.register(Report, ReportAdmin)
