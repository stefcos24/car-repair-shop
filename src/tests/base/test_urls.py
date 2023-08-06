from django.test import SimpleTestCase
from django.urls import reverse, resolve

from domain.views import domain_base


class TestBaseUrls(SimpleTestCase):

    def test_base_url_is_resolved(self):
        base_url = reverse("domain")
        self.assertEquals(resolve(base_url).func, domain_base)
