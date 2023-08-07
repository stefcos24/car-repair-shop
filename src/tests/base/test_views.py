from django.test import TestCase, Client
from django.urls import reverse

from tests.fixture_builder import FixtureBuilder
from tests.helpers import DataFixtureHelpers


class TestBaseViews(TestCase):
    fixtures = FixtureBuilder().person_user().build()

    def setUp(self):
        self.user = DataFixtureHelpers.get_admin_user()
        self.client = Client()
        self.client.force_login(user=self.user)

    def test_get_base(self):
        response = self.client.get(reverse("domain"))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "domain/index.html")

    def test_get_base_forbidden(self):
        self.client.logout()
        response = self.client.get(reverse("domain"))
        self.assertEquals(response.status_code, 302)
