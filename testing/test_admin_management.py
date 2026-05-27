from django.test import TestCase
from django.contrib.auth.models import User


class AdminManagementTest(TestCase):

    def setUp(self):
        self.admin = User.objects.create_superuser(
            username='admin',
            email='admin@gmail.com',
            password='Admin1234'
        )

    def test_admin_created(self):
        self.assertTrue(self.admin.is_superuser)

    def test_admin_login(self):
        login = self.client.login(
            username='admin',
            password='Admin1234'
        )

        self.assertTrue(login)

    def test_admin_panel_access(self):
        self.client.login(
            username='admin',
            password='Admin1234'
        )

        response = self.client.get('/admin/')

        self.assertEqual(response.status_code, 200)