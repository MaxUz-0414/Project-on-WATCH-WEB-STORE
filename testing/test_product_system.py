from django.test import TestCase
from store.models import Product, Category


class ProductSystemTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(
            title='Luxury',
            slug='luxury'
        )

        self.product = Product.objects.create(
            title='Rolex',
            slug='rolex',
            price=500,
            quantity=5,
            category=self.category
        )

    def test_product_created(self):
        self.assertEqual(self.product.title, 'Rolex')

    def test_product_price(self):
        self.assertTrue(self.product.price > 0)

    def test_product_quantity(self):
        self.assertTrue(self.product.quantity >= 0)

    def test_product_category(self):
        self.assertEqual(self.product.category, self.category)