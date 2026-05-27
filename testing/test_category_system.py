from django.test import TestCase
from store.models import Category


class CategorySystemTest(TestCase):

    def setUp(self):
        self.parent = Category.objects.create(
            title='Men',
            slug='men'
        )

        self.child = Category.objects.create(
            title='Sport',
            slug='sport',
            parent=self.parent
        )

    def test_category_creation(self):
        self.assertEqual(self.parent.title, 'Men')

    def test_subcategory_relationship(self):
        self.assertEqual(self.child.parent, self.parent)

    def test_category_slug(self):
        self.assertEqual(self.parent.slug, 'men')