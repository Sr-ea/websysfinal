from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class UserModelTests(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(username='testuser', password='pass123')
        self.assertEqual(user.username, 'testuser')
        self.assertTrue(user.check_password('pass123'))
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        admin = User.objects.create_superuser(username='admin', password='admin123')
        self.assertTrue(admin.is_staff)
        self.assertTrue(admin.is_superuser)

    def test_phone_number_blank_by_default(self):
        user = User.objects.create_user(username='user1', password='pass')
        self.assertEqual(user.phone_number, '')

    def test_user_str(self):
        user = User.objects.create_user(username='johndoe', password='pass')
        self.assertEqual(str(user), 'johndoe')
