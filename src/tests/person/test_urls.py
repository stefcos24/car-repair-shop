from django.test import SimpleTestCase
from django.urls import reverse, resolve

from domain.views import person_list, create_person, \
    get_or_update_person_details, delete_person


class TestPersonUrls(SimpleTestCase):

    def test_list_persons_url_is_resolved(self):
        persons_url = reverse("persons")
        self.assertEquals(resolve(persons_url).func, person_list)

    def test_create_person_url_is_resolved(self):
        create_person_url = reverse("person_create")
        self.assertEquals(resolve(create_person_url).func, create_person)

    def test_get_or_update_person_url_is_resolved(self):
        get_or_update_person_url = reverse(
            "person",
            kwargs={"person_id": "f77e2b40-acc4-4d74-aa20-18acefeb18fa"}
        )
        self.assertEquals(
            resolve(get_or_update_person_url).func,
            get_or_update_person_details
        )

    def test_delete_person_url_is_resolved(self):
        delete_person_url = reverse(
            "person_delete",
            kwargs={"person_id": "f77e2b40-acc4-4d74-aa20-18acefeb18fa"}
        )
        self.assertEquals(resolve(delete_person_url).func, delete_person)
