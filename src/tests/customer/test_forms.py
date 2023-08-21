from django.test import TestCase

from domain.forms.customer import CustomerForm


class TestCustomerForm(TestCase):
    def test_customer_form_valid_data(self):
        data = {
            "first_name": "John",
            "last_name": "Doe",
            "address1": "123 Main St",
            "address2": "Apt 4B",
            "city": "Springfield",
            "phone_number": "123-456-7890",
            "email": "john@example.com",
            "jib": "11111111111111",
            "pib": "411111111111111",
            "active": True,
        }
        form = CustomerForm(data=data)
        self.assertTrue(form.is_valid())

    def test_customer_form_part_data(self):
        data = {
            "first_name": "John",
            "last_name": "Doe",
            "address1": "123 Main St",
            "address2": "Apt 4B",
            "city": "Springfield",
        }
        form = CustomerForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)

    def test_customer_form_no_data(self):
        data = {}
        form = CustomerForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 8)
