from django.db import models

from domain.models import Person
from domain.models.customer import Customer
from domain.models.payments_details import PaymentsDetail


class Payment(models.Model):
    id = models.UUIDField(primary_key=True)
    person = models.ForeignKey(Person, on_delete=models.PROTECT)
    bill_id = models.CharField(max_length=50, null=False, db_index=True)
    payments_details = models.OneToOneField(
        PaymentsDetail,
        on_delete=models.PROTECT
    )
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    date_of_issue = models.DateTimeField(auto_now=True)
    value_date = models.DateTimeField(auto_now=True)
    delivery_date = models.DateTimeField(auto_now=True)
    payment_method = models.CharField(max_length=50, null=False)
    content = models.JSONField()

    def __str__(self):
        return f"Payment: " \
               f"{Payment.bill_id} " \
               f"{Customer.first_name} " \
               f"{Customer.last_name}"
