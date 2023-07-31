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

        widgets = {
            "first_name": forms.TextInput(
                attrs={"class": "form-control", "id": "inputFirstName",
                       "placeholder": "First Name"}
            ),
            "last_name": forms.TextInput(
                attrs={"class": "form-control", "id": "inputLastName",
                       "placeholder": "Last Name"}
            ),
            "address1": forms.TextInput(
                attrs={"class": "form-control", "id": "inputAddress",
                       "placeholder": "Address"}
            ),
            "address2": forms.TextInput(
                attrs={"class": "form-control", "id": "inputSecondAddress",
                       "placeholder": "SecondAddress"}
            ),
            "city": forms.TextInput(
                attrs={"class": "form-control", "id": "inputCity",
                       "placeholder": "City"}
            ),
            "phone_number": forms.TextInput(
                attrs={"class": "form-control", "id": "inputPhoneNumber",
                       "placeholder": "Phone Number"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "id": "inputEmail",
                       "placeholder": "Email"}
            ),
            "jib": forms.TextInput(
                attrs={"class": "form-control", "id": "inputJib",
                       "placeholder": "JIB"}
            ),
            "pib": forms.TextInput(
                attrs={"class": "form-control", "id": "inputPib",
                       "placeholder": "PIB"}
            ),
            "active": forms.Select(
                attrs={"class": "form-control custom-select",
                       "id": "inputActive", "placeholder": "Active"}
            ),
        }
