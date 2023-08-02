import uuid

from django.db import models
from django.utils import timezone
from djmoney.models.fields import MoneyField

from playground.utils import _choice


from django.contrib.auth import get_user_model

user_model = get_user_model()


class PaymentStatus(models.TextChoices):
    PENDING = _choice('Pending')
    PAID = _choice('Paid')
    REFUSED = _choice('Refused')


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(default=timezone.now)
    amount = MoneyField(max_digits=10, decimal_places=2, null=True,
                        default_currency=None)
    due_date = models.DateField()
    user = models.ForeignKey(user_model, on_delete=models.CASCADE)

    def __str__(self):
        return f'Order {self.id} - {self.status}'


class Payment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    external_id = models.CharField(max_length=100)
    authorization_id = models.CharField(max_length=100, null=True)
    amount = MoneyField(max_digits=10, decimal_places=2, null=True, default_currency=None)
    status = models.CharField(
        choices=PaymentStatus.choices,
        default=PaymentStatus.PENDING,
        max_length=20
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)