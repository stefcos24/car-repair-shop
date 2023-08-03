from django import forms
from django.forms import ModelForm
from domain.models.person import Person


class PersonForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "id": "inputPassword", "placeholder": "Password"}))

    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'active', 'password']

        widgets = {
            "first_name": forms.TextInput(
                attrs={"class": "form-control", "id": "inputFirstName", "placeholder": "First Name"}
            ),
            "last_name": forms.TextInput(
                attrs={"class": "form-control", "id": "inputLastName", "placeholder": "Last Name"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "form-control", "id": "inputEmail", "placeholder": "Email"}
            ),
            "phone_number": forms.TextInput(
                attrs={"class": "form-control", "id": "inputPhoneNumber", "placeholder": "Phone Number"}
            ),
            "active": forms.CheckboxInput(attrs={"name": "is active"})
        }
