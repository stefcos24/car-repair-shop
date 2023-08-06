from django.test import SimpleTestCase
from django.urls import reverse, resolve

from domain.views import customer_list, create_customer, \
    get_or_update_customer_details, delete_customer


class TestCustomerUrls(SimpleTestCase):

    def test_list_customers_url_is_resolved(self):
        customers_url = reverse("customers")
        self.assertEquals(resolve(customers_url).func, customer_list)

    def test_create_customer_url_is_resolved(self):
        create_customer_url = reverse("customer_create")
        self.assertEquals(resolve(create_customer_url).func, create_customer)

    def test_get_or_update_customer_url_is_resolved(self):
        get_or_update_customer_url = reverse(
            "customer",
            kwargs={"customer_id": "f77e2b40-acc4-4d74-aa20-18acefeb18fa"}
        )
        self.assertEquals(
            resolve(get_or_update_customer_url).func,
            get_or_update_customer_details
        )

    def test_delete_customer_url_is_resolved(self):
        delete_customer_url = reverse(
            "customer_delete",
            kwargs={"customer_id": "f77e2b40-acc4-4d74-aa20-18acefeb18fa"}
        )
        self.assertEquals(resolve(delete_customer_url).func, delete_customer)
