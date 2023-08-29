import uuid

from django.test import TestCase, Client
from django.urls import reverse

from domain.models import Person
from tests.fixture_builder import FixtureBuilder
from tests.helpers import DataFixtureHelpers


class TestPersonViews(TestCase):
    fixtures = FixtureBuilder().person_user().build()

    def setUp(self):
        self.user = DataFixtureHelpers.get_admin_user()
        self.client = Client()
        self.client.force_login(user=self.user)

    def test_get_persons_forbidden(self):
        self.client.logout()
        response = self.client.get(reverse("persons"))
        self.assertEqual(response.status_code, 302)

    def test_get_persons(self):
        response = self.client.get(reverse("persons"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "domain/persons.html")

    def test_create_person(self):
        data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john@example.com",
            "phone_number": "123-456-7890",
            "active": True,
            "password": "testpass",
        }
        response = self.client.post(reverse("person_create"), data)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("persons"))
        self.assertTrue(
            Person.objects.filter(email="john@example.com").exists()
        )

    def test_create_person_not_valid(self):
        data = {
            "last_name": "Doe",
            "email": "john@example.com",
            "phone_number": "123-456-7890",
            "active": 1,
        }
        response = self.client.post(reverse("person_create"), data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(
            Person.objects.filter(email="john@example.com").exists()
        )

    def test_get_person(self):
        response = self.client.get(reverse("persons"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "domain/persons.html")

    def test_get_person_details(self):
        person = Person.objects.filter(
            id="87e8bb82-7b76-4bcd-89be-2f4b3ff78187"
        ).first()

        response = self.client.get(
            reverse(
                "person",
                kwargs={"person_id": person.id},
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "domain/person.html")

    def test_get_person_details_not_exist(self):
        non_existent_id = uuid.uuid4()
        response = self.client.get(
            reverse(
                "person",
                kwargs={"person_id": non_existent_id},
            )
        )
        self.assertEqual(response.status_code, 404)

    def test_update_person_details_valid(self):
        person = Person.objects.filter(
            id="87e8bb82-7b76-4bcd-89be-2f4b3ff78187"
        ).first()

        data = {
            "first_name": "Updated",
            "last_name": "Doe",
            "email": "john@example.com",
            "phone_number": "123-456-7890",
            "active": True,
        }
        response = self.client.post(
            reverse(
                "person",
                kwargs={"person_id": person.id},
            ),
            data,
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("persons"))
        updated_person = Person.objects.get(id=person.id)
        self.assertEqual(updated_person.first_name, "Updated")

    def test_update_person_details_invalid(self):
        person = Person.objects.filter(
            id="87e8bb82-7b76-4bcd-89be-2f4b3ff78187"
        ).first()
        data = {
            "first_name": 234,
            "last_name": "",
            "address1": "",
        }
        response = self.client.post(
            reverse(
                "person",
                kwargs={"person_id": person.id},
            ),
            data,
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "domain/person.html")

    def test_get_or_update_person_details_not_logged_in(self):
        self.client.logout()
        person = Person.objects.filter(
            id="87e8bb82-7b76-4bcd-89be-2f4b3ff78187"
        ).first()
        response = self.client.get(
            reverse(
                "person",
                kwargs={"person_id": person.id},
            )
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            "/login/?next=/person/87e8bb82-7b76-4bcd-89be-2f4b3ff78187",
        )

    def test_delete_person_valid(self):
        person = Person.objects.filter(
            id="94296433-c66e-43af-af21-b495c11dd09b"
        ).first()
        response = self.client.post(
            reverse("person_delete", kwargs={"person_id": person.id})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("persons"))

        self.assertFalse(Person.objects.filter(id=person.id).exists())

    def test_delete_person_not_exist(self):
        non_existent_id = uuid.uuid4()
        response = self.client.post(
            reverse("customer_delete", kwargs={"customer_id": non_existent_id})
        )
        self.assertEqual(response.status_code, 404)

    def test_delete_person_get_request(self):
        person = Person.objects.filter(
            id="87e8bb82-7b76-4bcd-89be-2f4b3ff78187"
        ).first()
        response = self.client.get(
            reverse("person_delete", kwargs={"person_id": person.id})
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "domain/person_delete.html")

    def test_delete_person_not_logged_in(self):
        self.client.logout()
        person = Person.objects.filter(
            id="94296433-c66e-43af-af21-b495c11dd09b"
        ).first()
        response = self.client.post(
            reverse("person_delete", kwargs={"person_id": person.id})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            "/login/?next=/person/94296433-c66e-43af-af21-b495c11dd09b/delete",
        )
