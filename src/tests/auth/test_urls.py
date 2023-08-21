from django.test import SimpleTestCase
from django.urls import reverse, resolve

from domain.views import user_login, user_logout


class TestAuthUrls(SimpleTestCase):

    def test_user_login_url_is_resolved(self):
        auth_url = reverse("user_login")
        self.assertEquals(resolve(auth_url).func, user_login)

    def test_user_logout_url_is_resolved(self):
        auth_url = reverse("user_logout")
        self.assertEquals(resolve(auth_url).func, user_logout)
