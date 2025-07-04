from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase


class UserTest(APITestCase):

    """Test the User APIv2 endpoint."""

    fixtures = ["dojo_testdata.json"]

    def setUp(self):
        token = Token.objects.get(user__username="admin")
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)

    def test_user_list(self):
        r = self.client.get(reverse("user-list"))
        self.assertEqual(r.status_code, 200, r.content[:1000])
        user_list = r.json()["results"]
        self.assertGreaterEqual(len(user_list), 1, r.content[:1000])
        for user in user_list:
            for item in ["username", "first_name", "last_name", "email"]:
                self.assertIn(item, user, r.content[:1000])
            for item in ["password"]:
                self.assertNotIn(item, user, r.content[:1000])

    def test_user_add(self):
        # user with good password
        password = "testTEST1234!@#$"
        r = self.client.post(reverse("user-list"), {
            "username": "api-user-2",
            "email": "admin@dojo.com",
            "password": password,
        }, format="json")
        self.assertEqual(r.status_code, 201, r.content[:1000])

        # test password by fetching API key
        r = self.client.post(reverse("api-token-auth"), {
            "username": "api-user-2",
            "password": password,
        }, format="json")
        self.assertEqual(r.status_code, 200, r.content[:1000])

        # user with weak password
        r = self.client.post(reverse("user-list"), {
            "username": "api-user-3",
            "email": "admin@dojo.com",
            "password": "weakPassword",
        }, format="json")
        self.assertEqual(r.status_code, 400, r.content[:1000])
        self.assertIn("Password must contain at least 1 digit, 0-9.", r.content.decode("utf-8"))

    def test_user_change_password(self):
        # some user
        r = self.client.post(reverse("user-list"), {
            "username": "api-user-4",
            "email": "admin@dojo.com",
            "password": "testTEST1234!@#$",
        }, format="json")
        self.assertEqual(r.status_code, 201, r.content[:1000])
        user_id = r.json()["id"]

        r = self.client.put("{}{}/".format(reverse("user-list"), user_id), {
            "username": "api-user-4",
            "first_name": "first",
            "email": "admin@dojo.com",
        }, format="json")
        self.assertEqual(r.status_code, 200, r.content[:1000])

        r = self.client.patch("{}{}/".format(reverse("user-list"), user_id), {
            "last_name": "last",
            "email": "admin@dojo.com",
        }, format="json")
        self.assertEqual(r.status_code, 200, r.content[:1000])

        r = self.client.put("{}{}/".format(reverse("user-list"), user_id), {
            "username": "api-user-4",
            "email": "admin@dojo.com",
            "password": "testTEST1234!@#$",
        }, format="json")
        self.assertEqual(r.status_code, 400, r.content[:1000])
        self.assertIn("Update of password though API is not allowed", r.content.decode("utf-8"))

        r = self.client.patch("{}{}/".format(reverse("user-list"), user_id), {
            "password": "testTEST1234!@#$",
            "email": "admin@dojo.com",
        }, format="json")
        self.assertEqual(r.status_code, 400, r.content[:1000])
        self.assertIn("Update of password though API is not allowed", r.content.decode("utf-8"))

    def test_user_deactivate(self):
        # user with good password
        password = "testTEST1234!@#$"
        r = self.client.post(reverse("user-list"), {
            "username": "api-user-10",
            "email": "admin@dojo.com",
            "password": password,
        }, format="json")
        self.assertEqual(r.status_code, 201, r.content[:1000])

        # user with good password
        password = "testTEST1234!@#$"
        r = self.client.post(reverse("user-list"), {
            "username": "api-user-2",
            "email": "admin@dojo.com",
            "password": password,
        }, format="json")
        self.assertEqual(r.status_code, 201, r.content[:1000])
        user_id = r.json()["id"]

        # deactivate
        r = self.client.patch("{}{}/".format(reverse("user-list"), user_id), {
            "is_active": False,
        }, format="json")
        self.assertEqual(r.status_code, 200, r.content[:1000])

        # check is_active field
        r = self.client.get("{}{}/".format(reverse("user-list"), user_id))
        self.assertEqual(r.status_code, 200, r.content[:1000])
        self.assertEqual(r.json()["is_active"], False, r.content[:1000])

        # API key retrieval should fail for inactive user
        r = self.client.post(reverse("api-token-auth"), {
            "username": "api-user-2",
            "password": password,
        }, format="json")
        self.assertEqual(r.status_code, 400, r.content[:1000])
