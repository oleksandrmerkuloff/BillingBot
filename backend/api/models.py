import uuid
from decimal import Decimal

from django.db import models
from django.core.validators import MinValueValidator


class Meter(models.Model):
    id = models.UUIDField(
        editable=False,
        primary_key=True,
        default=uuid.uuid4
    )
    name = models.CharField(max_length=50, unique=True)
    meter_number = models.CharField(
        max_length=50,
        unique=True,
        null=True,
        blank=True
        )
    price_per_unit = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        blank=True,
        default=Decimal(0.00),
        validators=[MinValueValidator(0)]
    )
    unit_name = models.CharField(max_length=30)
    total_consumed = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0)]
        )
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Meter'
        verbose_name_plural = 'Meters'
        ordering = ['name']


class Report(models.Model):
    id = models.UUIDField(
        editable=False,
        primary_key=True,
        default=uuid.uuid4
        )
    created_at = models.DateTimeField(
        editable=False,
        auto_now_add=True
        )
    bill = models.FileField(
        null=True,
        blank=True,
        upload_to='bills/%Y/%m/'
    )

    @property
    def is_paid(self):
        if self.bill is None:
            return False
        return True

    @property
    def total(self):
        items = self.items.all()
        return sum([item.total for item in items])

    def __str__(self) -> str:
        month = self.created_at.month
        year = self.created_at.year
        return f'Report for the {month} of {year}'

    class Meta:
        verbose_name = 'Report'
        verbose_name_plural = 'Reports'
        ordering = ['-created_at']


class ReportItem(models.Model):
    id = models.UUIDField(
        editable=False,
        primary_key=True,
        default=uuid.uuid4
    )
    meter = models.ForeignKey(
        Meter,
        on_delete=models.DO_NOTHING,
        related_name='items'
        )
    report = models.ForeignKey(
        Report,
        on_delete=models.CASCADE,
        related_name='items'
        )
    consume = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    created_at = models.DateField(auto_now_add=True, editable=False)

    @property
    def total(self):
        return round(self.consume * self.meter.price_per_unit, 2)

    def __str__(self) -> str:
        if self.report.is_paid:
            return f'You paid {self.total} for {self.meter.name}.'
        return f'You need to pay {self.total} for {self.meter.name}.'

    class Meta:
        verbose_name = 'Report Item'
        verbose_name_plural = 'Report Items'
        ordering = ['-created_at', 'total']
