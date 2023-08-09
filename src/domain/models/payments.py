from django.db import models

from domain.models import Person
from domain.models.customer import Customer
from domain.models.payments_details import PaymentsDetail


class Payment(models.Model):
    id = models.UUIDField(primary_key=True)
    person = models.ForeignKey(Person, on_delete=models.PROTECT)
    bill_id = models.IntegerField(unique=True, null=False, default=1)
    payments_details = models.OneToOneField(
        PaymentsDetail, on_delete=models.PROTECT
    )
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    vehicle = models.CharField(max_length=50, null=True)
    vehicle_plate_number = models.CharField(max_length=50, null=True)
    date_of_issue = models.DateTimeField(auto_now=True)
    value_date = models.DateTimeField(auto_now=True)
    delivery_date = models.DateTimeField(auto_now=True)
    payment_method = models.CharField(max_length=50, null=False)
    content = models.JSONField()

    def __str__(self):
        return f"Payment: {self.id}"
