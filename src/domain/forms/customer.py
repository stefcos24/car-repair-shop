from django import forms
from django.forms import ModelForm
from domain.models.customer import Customer


class CustomerForm(ModelForm):

    class Meta:
        model = Customer
        fields = [
            "first_name",
            "last_name",
            "address1",
            "address2",
            "city",
            "phone_number",
            "email",
            "jib",
            "pib",
            "active"
        ]
