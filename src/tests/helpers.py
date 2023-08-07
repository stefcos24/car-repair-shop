from django.contrib.auth.models import User


class DataFixtureHelpers:
    TEST_USER_ADMIN = "admin_user"
    TEST_USER_STAFF = "staff_user"

    TEST_CUSTOMER_1 = "8df03853-c308-4d09-810c-5828774d9800"
    TEST_CUSTOMER_2 = "dd1d65ec-c7ca-4153-be3d-0448172447bf"
    TEST_CUSTOMER_3 = "481a0f51-d8f6-42bb-88c9-fe424620f321"
    TEST_CUSTOMER_4 = "30fc61d0-d6ff-4ff3-89a5-688938119d26"
    TEST_CUSTOMER_5 = "1af80e45-0439-4cda-b905-81eb9c303afe"
    TEST_CUSTOMER_6 = "f984f05b-d1ca-41d7-b5d5-0ec7f2a9504b"
    TEST_CUSTOMER_7 = "5b8c4f2e-ec33-4a40-a2df-62fe26c6175b"
    TEST_CUSTOMER_8 = "a5b6a162-6070-458d-9925-6773681064ac"
    TEST_CUSTOMER_9 = "83a4d9c2-4569-4c8e-9a37-aefe40d2b587"
    TEST_CUSTOMER_10 = "5b8c4f2e-ec33-4a40-a2df-62fe26c6175b"
    TEST_CUSTOMER_11 = "7b4a58a7-8eeb-4dab-b001-5952af4e2fa1"

    @classmethod
    def get_admin_user(cls, username=TEST_USER_ADMIN) -> User:
        return User.objects.get(username=username)

    @classmethod
    def get_staff_user(cls, username=TEST_USER_STAFF) -> User:
        return User.objects.get(username=username)
