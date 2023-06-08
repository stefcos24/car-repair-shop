from django.db import models
from django.contrib.auth.models import User


class Person(models.Model):
    id = models.UUIDField(primary_key=True)
    first_name = models.CharField(max_length=50, null=False, db_index=True)
    last_name = models.CharField(max_length=50, null=False, db_index=True)
    email = models.CharField(max_length=60, null=False, unique=True)
    phone_number = models.CharField(max_length=30, blank=True, null=False)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        related_name="person",
        null=True,
        blank=True
    )

    def __str__(self):
        return f"Person: {self.first_name} {self.last_name}"
