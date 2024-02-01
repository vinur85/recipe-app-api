"""
Test for models
"""
from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test Models."""

    def test_create_user_with_email_successful(self):
        """Test creating user with email is successful."""
        email = 'example@example.com'
        password = 'example@123'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test if email address normalized"""
        sample_email_addresses = [
            ['test1@example.com', 'test1@example.com'],
            ['test2@EXAMPLE.COM', 'test2@example.com'],
            ['Test3@example.com', 'Test3@example.com'],
            ['TEST4@EXAMPLE.COM', 'TEST4@example.com'],
        ]

        for email, expected in sample_email_addresses:
            user = get_user_model().objects.create_user(email, 'Sample123')
            self.assertEqual(expected, user.email)

    def test_new_user_email_normalized(self):
        """Test if empty email address during creation raises ValueError"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'Sample123')

    def test_create_super_user(self):
        """Test create superuser"""
        user = get_user_model().objects.create_superuser(
            'admin@example.com',
            'Super@12345'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
