import uuid

from django.db import models


class Bill(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=6, decimal_places=2)
    paid = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self) -> str:
        if self.paid:
            return f'Bill for the {self.created_at.month}, total: {self.total}, paid.'
        return f'Bill for the {self.created_at.month}, total: {self.total}, not paid.'


class Counter(models.Model):
    id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=75)
    number = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class CounterRecord(models.Model):
    created_at = models.DateField(auto_now_add=True)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    counter = models.ForeignKey(
        Counter,
        on_delete=models.CASCADE,
        related_name='records'
        )

    def __str__(self) -> str:
        return f'{self.counter}: {self.amount} for the {self.created_at.month}'
