from django.test import TestCase
from django.urls import reverse


class URLSystemTest(TestCase):

    def test_product_list_url(self):
        response = self.client.get(reverse('product_list'))
        self.assertNotEqual(response.status_code, 404)

    def test_login_url(self):
        response = self.client.get(reverse('login'))
        self.assertNotEqual(response.status_code, 404)

    def test_register_url(self):
        response = self.client.get(reverse('register'))
        self.assertNotEqual(response.status_code, 404)