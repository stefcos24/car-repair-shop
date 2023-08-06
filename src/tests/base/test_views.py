from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse


class TestBaseViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass"
        )
        self.client = Client()
        self.client.login(
            username="testuser",
            password="testpass"
        )

    def test_get_base(self):
        response = self.client.get(reverse("domain"))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "domain/index.html")
