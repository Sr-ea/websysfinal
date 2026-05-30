from django.test import TestCase, RequestFactory
from catalog.models import Category, Product
from cart.cart import Cart


class CartTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.category = Category.objects.create(name='Fruits', slug='fruits')
        self.product = Product.objects.create(
            category=self.category,
            name='Banana',
            price=65.00,
            stock=100,
        )

    def _get_cart(self):
        request = self.factory.get('/')
        request.session = self.client.session
        return Cart(request)

    def test_cart_is_empty_initially(self):
        cart = self._get_cart()
        self.assertEqual(len(cart), 0)

    def test_add_product(self):
        cart = self._get_cart()
        cart.add(self.product)
        self.assertEqual(len(cart), 1)

    def test_add_product_with_quantity(self):
        cart = self._get_cart()
        cart.add(self.product, quantity=3)
        self.assertEqual(len(cart), 3)

    def test_add_same_product_increases_quantity(self):
        cart = self._get_cart()
        cart.add(self.product, quantity=2)
        cart.add(self.product, quantity=3)
        self.assertEqual(len(cart), 5)

    def test_override_quantity(self):
        cart = self._get_cart()
        cart.add(self.product, quantity=2)
        cart.add(self.product, quantity=5, override_quantity=True)
        self.assertEqual(len(cart), 5)

    def test_remove_product(self):
        cart = self._get_cart()
        cart.add(self.product)
        cart.remove(self.product)
        self.assertEqual(len(cart), 0)

    def test_get_total(self):
        cart = self._get_cart()
        cart.add(self.product, quantity=2)
        self.assertEqual(cart.get_total(), 130.00)

    def test_clear_cart(self):
        cart = self._get_cart()
        cart.add(self.product)
        cart.clear()
        self.assertEqual(len(cart), 0)
