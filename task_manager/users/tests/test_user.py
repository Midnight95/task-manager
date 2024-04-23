from django.urls import reverse_lazy
from task_manager.users.models import User
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
            User.objects.get(username=data['email'])


class TestUserRead(UserTestCase):
    def setUp(self):
        self.user = User.objects.create_user(**self.test_data['read']['login'])

    def test_user_login_url(self):
        response = self.client.get(reverse_lazy('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='forms/form.html')

    def test_login(self):
        username = self.test_data['read']['login']['username']
        password = self.test_data['read']['login']['password']
        response = self.client.post(
                reverse_lazy('login'),
                data={'username': username, 'password': password},
                follow=True
                )

        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse_lazy('home'))
        self.assertTrue(response.context['user'].is_authenticated)

    def test_invalid_credentials(self):
        user_credentials = self.test_data['read']['invalid_login']
        response = self.client.post(
            reverse_lazy('login'),
            data=user_credentials
        )

        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse_lazy('home'))
        self.assertContains(response, 'logout')

        response = self.client.post(reverse_lazy('logout'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'logout')


class TestUserUpdate(UserTestCase):

    def test_valid_update(self):
        user = User.objects.get(pk=1)
        self.client.force_login(user)
        data = self.test_data['update']

        response = self.client.post(
           reverse_lazy('update_user', kwargs={'pk': 1}),
           data=data,
           )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, expected_url=reverse_lazy('users'))

        response = self.client.get(reverse_lazy('users'))
        self.assertContains(response, data['username'])

    def test_update_wrong_user(self):
        user = User.objects.get(pk=1)
        self.client.force_login(user)
        data = self.test_data['update']

        response = self.client.post(
           reverse_lazy('update_user', kwargs={'pk': 2}),
           data=data,
           )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, expected_url=reverse_lazy('home'))

        response = self.client.get(reverse_lazy('users'))
        self.assertNotContains(response, data['username'])

    def test_update_not_logged_in(self):
        data = self.test_data['update']
        response = self.client.post(
           reverse_lazy('update_user', kwargs={'pk': 1}),
           data=data,
           )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, expected_url=reverse_lazy('home'))

        self.assertNotContains(
            self.client.get(reverse_lazy('users')),
            data['username']
            )


class TestUserDeletion(UserTestCase):

    def test_delete_self(self):
        user = User.objects.get(pk=1)
        self.client.force_login(user)
        response = self.client.post(
            reverse_lazy('delete_user', kwargs={'pk': 1})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, expected_url=reverse_lazy('users'))
        self.assertNotContains(
            self.client.get(reverse_lazy('users')),
            user.username
        )

    def test_delete_wrong_user(self):
        user = User.objects.get(pk=1)
        self.client.force_login(user)
        response = self.client.post(
            reverse_lazy('delete_user', kwargs={'pk': 2})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, expected_url=reverse_lazy('home'))
        self.assertContains(
            self.client.get(reverse_lazy('users')),
            user.username
        )

    def test_delete_not_logged_in(self):
        user = User.objects.get(pk=1)
        response = self.client.post(
            reverse_lazy('delete_user', kwargs={'pk': 1})
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, expected_url=reverse_lazy('home'))
        self.assertContains(
            self.client.get(reverse_lazy('users')),
            user.username
        )
