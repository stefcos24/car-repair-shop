from django.db import models


class Customer(models.Model):
    id = models.UUIDField(primary_key=True)
    full_name = models.CharField(max_length=50, null=False, db_index=True)
    first_name = models.CharField(max_length=50, null=False, db_index=True)
    last_name = models.CharField(max_length=50, null=False, db_index=True)
    address1 = models.CharField(max_length=60, null=False, unique=True)
    address2 = models.CharField(max_length=60)
    city = models.CharField(max_length=60, null=False)
    phone_number = models.CharField(max_length=30, blank=True, null=False)
    email = models.CharField(max_length=60, null=False, unique=True)
    JIB = models.CharField(max_length=60, null=False, unique=True)
    PIB = models.CharField(max_length=60, null=False, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"Customer: {self.first_name} {self.last_name}"
