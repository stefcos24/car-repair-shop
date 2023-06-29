from django.db import models
from .payments import *


class Payments_items(models.Model):
    id=models.UUIDField(primary_key=True)
    payment=models.ForeignKey(Payments, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)