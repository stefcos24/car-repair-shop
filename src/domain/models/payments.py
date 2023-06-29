from django.db import models
from .customer import *
from .person import *
from .payments_details import *

class Payments(models.Model):
    id=models.UUIDField(primary_key=True)
    person=models.ForeignKey(Person, related_name="payments", on_delete=models.CASCADE)
    bill_id=models.CharField(max_length=50, null=False, db_index=True)
    payments_details=models.OneToOneField(Payments_details, related_name="payments", on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer, related_name="payments", on_delete=models.CASCADE)
    date_of_issue=models.DateTimeField(auto_now=True)
    value_date=models.DateTimeField(auto_now=True)
    delivery_date=models.DateTimeField(auto_now=True)
    payment_method=models.CharField(max_length=50, null=False)
    content=models.JSONField()
    
    def __str__(self):
        return f"Paymant: {Customer.first_name} {Customer.last_name}"