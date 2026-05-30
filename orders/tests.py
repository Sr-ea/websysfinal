from django.test import TestCase
from django.contrib.auth import get_user_model
from catalog.models import Category, Product
from orders.models import Order, OrderItem

User = get_user_model()


class OrderModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='customer', password='pass')
        self.category = Category.objects.create(name='Fruits', slug='fruits')
        self.product = Product.objects.create(
            category=self.category,
            name='Banana',
            price=65.00,
            stock=100,
        )

    def test_create_order(self):
        order = Order.objects.create(
            user=self.user,
            full_name='John Doe',
            email='john@example.com',
            address='123 Main St',
            city='Manila',
            postal_code='1000',
            total=130.00,
        )
        self.assertEqual(order.status, 'pending')
        self.assertEqual(order.full_name, 'John Doe')
        self.assertIn('Order', str(order))

    def test_order_default_status(self):
        order = Order.objects.create(
            user=self.user,
            full_name='Jane Doe',
            email='jane@example.com',
            address='456 Oak Ave',
            city='Cebu',
            postal_code='6000',
            total=65.00,
        )
        self.assertEqual(order.status, 'pending')

    def test_create_order_item(self):
        order = Order.objects.create(
            user=self.user,
            full_name='John Doe',
            email='john@example.com',
            address='123 Main St',
            city='Manila',
            postal_code='1000',
            total=65.00,
        )
        item = OrderItem.objects.create(
            order=order,
            product=self.product,
            product_name='Banana',
            price=65.00,
            quantity=1,
        )
        self.assertEqual(str(item), '1x Banana')
        self.assertEqual(item.order, order)

    def test_order_items_relation(self):
        order = Order.objects.create(
            user=self.user,
            full_name='John Doe',
            email='john@example.com',
            address='123 Main St',
            city='Manila',
            postal_code='1000',
            total=130.00,
        )
        OrderItem.objects.create(order=order, product=self.product, product_name='Banana', price=65.00, quantity=2)
        self.assertEqual(order.items.count(), 1)

    def test_order_ordering(self):
        order1 = Order.objects.create(
            user=self.user,
            full_name='A',
            email='a@a.com',
            address='Addr',
            city='City',
            postal_code='0000',
            total=10.00,
        )
        order2 = Order.objects.create(
            user=self.user,
            full_name='B',
            email='b@b.com',
            address='Addr',
            city='City',
            postal_code='0000',
            total=20.00,
        )
        qs = Order.objects.all()
        self.assertEqual(qs.first(), order2)
        self.assertEqual(qs.last(), order1)
