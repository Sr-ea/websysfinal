from django.test import TestCase
from catalog.models import Category, Product


class CategoryModelTests(TestCase):
    def test_create_category(self):
        cat = Category.objects.create(name='Fruits', slug='fruits', description='Fresh fruits')
        self.assertEqual(cat.name, 'Fruits')
        self.assertEqual(cat.slug, 'fruits')

    def test_category_str(self):
        cat = Category.objects.create(name='Dairy', slug='dairy')
        self.assertEqual(str(cat), 'Dairy')

    def test_category_verbose_name_plural(self):
        self.assertEqual(Category._meta.verbose_name_plural, 'categories')


class ProductModelTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Fruits', slug='fruits')

    def test_create_product(self):
        product = Product.objects.create(
            category=self.category,
            name='Banana',
            price=65.00,
            stock=100,
        )
        self.assertEqual(product.name, 'Banana')
        self.assertEqual(product.price, 65.00)
        self.assertTrue(product.available)

    def test_product_str(self):
        product = Product.objects.create(
            category=self.category,
            name='Apple',
            price=90.00,
            stock=50,
        )
        self.assertEqual(str(product), 'Apple')

    def test_product_default_stock_zero(self):
        product = Product.objects.create(
            category=self.category,
            name='Test',
            price=10.00,
        )
        self.assertEqual(product.stock, 0)

    def test_product_belongs_to_category(self):
        product = Product.objects.create(
            category=self.category,
            name='Carrot',
            price=55.00,
            stock=60,
        )
        self.assertEqual(product.category, self.category)


class CatalogViewTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='Fruits', slug='fruits')
        self.product = Product.objects.create(
            category=self.category,
            name='Banana',
            price=65.00,
            stock=100,
        )

    def test_product_list_loads(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Banana')

    def test_product_detail_loads(self):
        response = self.client.get(f'/product/{self.product.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Banana')

    def test_category_filter(self):
        response = self.client.get('/?category=fruits')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Banana')

    def test_search(self):
        response = self.client.get('/?q=Banana')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Banana')

    def test_search_no_results(self):
        response = self.client.get('/?q=NonExistentProduct')
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'Banana')
