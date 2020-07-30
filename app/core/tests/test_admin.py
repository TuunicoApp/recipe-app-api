from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

# https://docs.djangoproject.com/en/2.2/topics/testing/tools/#overview-and-a-quick-example


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()  # Create Client
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@londonappdev.com',
            password='password123'
        )  # Create Admin
        self.client.force_login(self.admin_user)  # Log Admin to the system
        self.user = get_user_model().objects.create_user(
            email='test@londonappdev.com',
            password='password123',
            name='Test user full name'
        )  # Create a spare user

    def test_users_listed(self):
        """Test that users are listed on user page"""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)  # Will pull out the url for the user

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Test that the user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
        # validates with the 200 that the response was OK.

    def test_create_user_page(self):
        """Test that the create user page works"""
        url = reverse('admin:core_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
