from django.urls import reverse_lazy
from task_manager.user.models import User
from .user_setup import UserTestCase


class TestUserCreation(UserTestCase):
    def test_user_creation_url(self):
        response = self.client.get(reverse_lazy('user_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='forms/form.html')

    def test_valid_user_creation(self):
        data = self.test_data['create']['valid']
        response = self.client.post(
                reverse_lazy('user_create'), data=data
                )
        self.assertRedirects(response, expected_url=reverse_lazy('login'))
        self.assertEqual(response.status_code, 302)
        user = User.objects.get(username=data['username'])
        self.assertTrue(user.is_active)

    def test_non_unique_email(self):
        data = self.test_data['create']['invalid_email']
        response = self.client.post(
                reverse_lazy('user_create'), data=data
                )
        self.assertEqual(response.status_code, 200)
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(username=data['username'])

    def test_non_unique_username(self):
        data = self.test_data['create']['invalid_username']
        response = self.client.post(
                reverse_lazy('user_create'), data=data
                )
        self.assertEqual(response.status_code, 200)
        with self.assertRaises(User.DoesNotExist):
            User.objects.get(username=data['username'])


class TestUserReading(UserTestCase):
    def setUp(self):
        self.user_credentials = {
            'username': 'login_user',
            'password': 'lup@ssW@rd'
        }
        self.user = User.objects.create_user(**self.user_credentials)

    def test_user_login_url(self):
        response = self.client.get(reverse_lazy('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='forms/form.html')

    def test_login(self):
        response = self.client.post(
                reverse_lazy('login'), data=self.user_credentials, follow=True
                )

        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse_lazy('home'))
        self.assertTrue(response.context['user'].is_authenticated)

    def test_logout(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse_lazy('home'))
        self.assertContains(response, 'logout')

        response = self.client.post(reverse_lazy('logout'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'logout')
