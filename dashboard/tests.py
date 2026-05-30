from django.test import TestCase
from django.contrib.auth import get_user_model
from catalog.models import Category, Product
from orders.models import Order

User = get_user_model()


class DashboardViewTests(TestCase):
    def setUp(self):
        self.staff = User.objects.create_user(username='staff', password='pass', is_staff=True)
        self.user = User.objects.create_user(username='customer', password='pass')

    def test_dashboard_requires_staff(self):
        self.client.login(username='customer', password='pass')
        response = self.client.get('/dashboard/')
        self.assertEqual(response.status_code, 302)

    def test_dashboard_loads_for_staff(self):
        self.client.login(username='staff', password='pass')
        response = self.client.get('/dashboard/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Dashboard')

    def test_dashboard_products(self):
        self.client.login(username='staff', password='pass')
        response = self.client.get('/dashboard/products/')
        self.assertEqual(response.status_code, 200)

    def test_dashboard_orders(self):
        self.client.login(username='staff', password='pass')
        response = self.client.get('/dashboard/orders/')
        self.assertEqual(response.status_code, 200)
