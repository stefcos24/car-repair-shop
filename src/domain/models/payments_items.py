from django.db import models

from domain.models import Payment


class PaymentsItem(models.Model):
    id = models.UUIDField(primary_key=True)
    payment = models.ForeignKey(Payment, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Payment item: {PaymentsItem.id}"
