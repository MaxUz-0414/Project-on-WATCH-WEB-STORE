from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


class AuthenticationTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='Test1234'
        )

    def test_login_url_loads(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_register_url_loads(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def test_user_login(self):
        login = self.client.login(
            username='testuser',
            password='Test1234'
        )

        self.assertTrue(login)

    def test_logout_system(self):
        self.client.login(
            username='testuser',
            password='Test1234'
        )

        response = self.client.get(reverse('logout'))
        self.assertNotEqual(response.status_code, 500)