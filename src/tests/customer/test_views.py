import uuid

from django.test import TestCase, Client
from django.urls import reverse

from domain.models import Customer
from tests.fixture_builder import FixtureBuilder
from tests.helpers import DataFixtureHelpers


class TestCustomerViews(TestCase):
    fixtures = FixtureBuilder().person_user().customer().build()

    def setUp(self):
        self.user = DataFixtureHelpers.get_admin_user()
        self.client = Client()
        self.client.force_login(user=self.user)

    def test_get_customers_forbidden(self):
        self.client.logout()
        response = self.client.get(reverse("customers"))
        self.assertEquals(response.status_code, 302)

    def test_get_customers(self):
        response = self.client.get(reverse("customers"))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "domain/customers.html")

    def test_create_customer(self):
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
        response = self.client.post(reverse("customer_create"), data)

        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, reverse("customers"))
        self.assertTrue(
            Customer.objects.filter(email="john@example.com").exists()
        )

    def test_create_customer_not_valid(self):
        data = {
            "first_name": "John",
            "last_name": "Doe",
            "address1": "123 Main St",
            "email": "john@example.com",
        }
        response = self.client.post(reverse("customer_create"), data)
        self.assertEquals(response.status_code, 200)
        self.assertFalse(
            Customer.objects.filter(email="john@example.com").exists()
        )

    def test_get_customer(self):
        response = self.client.get(reverse("customers"))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "domain/customers.html")

    def test_get_customer_details(self):
        customer = Customer.objects.filter(
            id="8df03853-c308-4d09-810c-5828774d9800"
        ).first()

        response = self.client.get(
            reverse(
                "customer",
                kwargs={"customer_id": customer.id},
            )
        )
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "domain/customer.html")

    def test_get_customer_details_not_exist(self):
        non_existent_id = uuid.uuid4()
        response = self.client.get(
            reverse(
                "customer",
                kwargs={"customer_id": non_existent_id},
            )
        )
        self.assertEquals(response.status_code, 404)

    def test_update_customer_details_valid(self):
        customer = Customer.objects.filter(
            id="8df03853-c308-4d09-810c-5828774d9800"
        ).first()

        data = {
            "first_name": "Updated",
            "last_name": "Name",
            "address1": "456 Another St",
            "address2": "Apt 5C",
            "city": "Another City",
            "phone_number": "789-123-4560",
            "email": "updated@example.com",
            "jib": "22222222222222",
            "pib": "422222222222222",
            "active": False,
        }
        response = self.client.post(
            reverse(
                "customer",
                kwargs={"customer_id": customer.id},
            ),
            data,
        )

        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, reverse("customers"))
        updated_customer = Customer.objects.get(id=customer.id)
        self.assertEquals(updated_customer.first_name, "Updated")

    def test_update_customer_details_invalid(self):
        customer = Customer.objects.filter(
            id="8df03853-c308-4d09-810c-5828774d9800"
        ).first()
        data = {
            "first_name": "",
            "last_name": "",
            "address1": "",
            # ... provide invalid data
        }
        response = self.client.post(
            reverse(
                "customer",
                kwargs={"customer_id": customer.id},
            ),
            data,
        )
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "domain/customer.html")

    def test_get_or_update_customer_details_not_logged_in(self):
        self.client.logout()
        customer = Customer.objects.filter(
            id="8df03853-c308-4d09-810c-5828774d9800"
        ).first()
        response = self.client.get(
            reverse(
                "customer",
                kwargs={"customer_id": customer.id},
            )
        )
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(
            response,
            "/login/?next=/customer/8df03853-c308-4d09-810c-5828774d9800",
        )

    def test_delete_customer_valid(self):
        customer = Customer.objects.filter(
            id="dd1d65ec-c7ca-4153-be3d-0448172447bf"
        ).first()

        response = self.client.post(
            reverse("customer_delete", kwargs={"customer_id": customer.id})
        )

        self.assertEquals(response.status_code, 302)
        self.assertRedirects(response, reverse("customers"))

        self.assertFalse(Customer.objects.filter(id=customer.id).exists())

    def test_delete_customer_not_exist(self):
        non_existent_id = uuid.uuid4()
        response = self.client.post(
            reverse("customer_delete", kwargs={"customer_id": non_existent_id})
        )
        self.assertEquals(response.status_code, 404)

    def test_delete_customer_get_request(self):
        customer = Customer.objects.filter(
            id="dd1d65ec-c7ca-4153-be3d-0448172447bf"
        ).first()
        response = self.client.get(
            reverse("customer_delete", kwargs={"customer_id": customer.id})
        )

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "domain/customer_delete.html")

    def test_delete_customer_not_logged_in(self):
        self.client.logout()
        customer = Customer.objects.filter(
            id="dd1d65ec-c7ca-4153-be3d-0448172447bf"
        ).first()
        response = self.client.post(
            reverse("customer_delete", kwargs={"customer_id": customer.id})
        )
        self.assertEquals(response.status_code, 302)
        self.assertRedirects(
            response,
            "/login/?next=/customer/dd1d65ec-c7ca-4153-be3d-0448172447bf/delete",
        )
