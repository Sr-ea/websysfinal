from django.test import TestCase
from django.contrib.auth import get_user_model
from catalog.models import Category, Product

User = get_user_model()


class CheckoutViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='customer', password='pass')
        self.category = Category.objects.create(name='Fruits', slug='fruits')
        self.product = Product.objects.create(
            category=self.category,
            name='Banana',
            price=65.00,
            stock=100,
        )
        session = self.client.session
        session['cart'] = {str(self.product.id): {'quantity': 2, 'price': '65.00'}}
        session.save()

    def test_checkout_get_requires_login(self):
        response = self.client.get('/checkout/')
        self.assertRedirects(response, '/accounts/login/?next=/checkout/')

    def test_checkout_page_loads_when_logged_in(self):
        self.client.login(username='customer', password='pass')
        response = self.client.get('/checkout/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Checkout')

    def test_checkout_post_creates_order(self):
        self.client.login(username='customer', password='pass')
        response = self.client.post('/checkout/', {
            'full_name': 'John Doe',
            'email': 'john@example.com',
            'address': '123 Main St',
            'city': 'Manila',
            'postal_code': '1000',
            'country': 'Philippines',
        })
        self.assertRedirects(response, '/checkout/success/1/', fetch_redirect_response=False)

    def test_checkout_empty_cart(self):
        self.client.login(username='customer', password='pass')
        session = self.client.session
        session['cart'] = {}
        session.save()
        response = self.client.get('/checkout/')
        self.assertRedirects(response, '/')
