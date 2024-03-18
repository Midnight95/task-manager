from django.test import TestCase
from django.urls import reverse_lazy
from task_manager.user.models import User
from task_manager.status.models import Status


class TestStatusIndx(TestCase):

    def test_status_page(self):
        response = self.client.get(reverse_lazy('status_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, tempate_name='status/statuses.html')


class TestStatusCRUD(TestCase):
    def setUp(self):
        self.user_credentials = {
            'username': 'login_user',
            'password': 'lup@ssW@rd'
        }
        self.user = User.objects.create_user(**self.user_credentials)
        self.client.force_login(self.user)

        self.status_data = {'name': '1st'}
        Status.objects.create(**self.status_data)

    def test_status_creation(self):
        response = self.client.post(
                reverse_lazy('status_create'),
                data=self.status_data
                )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('statuses'))
        self.assertEqual(len(Status.objects.all()), 2)

    def test_status_deletion(self):
        response = self.client.post(
                reverse_lazy('status_delete', kwargs={'pk': 1})
                )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('statuses'))
        self.assertEqual(len(Status.objects.all()), 0)

    def test_status_update(self):
        response = self.client.post(
                reverse_lazy('status_update', kwargs={'pk': 1}),
                data={'name': 'updated'},
                follow=True
                )

        self.assertContains(response, 'updated')
