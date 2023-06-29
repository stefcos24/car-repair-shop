from django.db import models

class Payments_details(models.Model):
    id=models.UUIDField(primary_key=True)
    total_amount=models.CharField(max_length=50, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)