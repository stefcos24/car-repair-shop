from django.test import TestCase

from domain.forms.person import PersonForm


class TestPersonForm(TestCase):
    def test_person_form_valid_data(self):
        data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john@example.com",
            "phone_number": "066111222",
            "active": True,
            "password": "test-password",
        }
        form = PersonForm(data=data)
        self.assertTrue(form.is_valid())

    def test_person_form_part_data(self):
        data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john@example.com",
        }
        form = PersonForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 1)

    def test_customer_form_no_data(self):
        data = {}
        form = PersonForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 4)
