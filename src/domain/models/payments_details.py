from django.db import models


class PaymentsDetail(models.Model):
    id = models.UUIDField(primary_key=True)
    total_amount = models.CharField(max_length=50, null=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Payment detail: " f"{self.id} - " f"{self.total_amount}"
