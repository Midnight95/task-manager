from django.test import TestCase
from django.urls import reverse_lazy
from task_manager.user.models import User
from task_manager.task.models import Task


class TestTaskCRUD(TestCase):
    def setUp(self):
        self.user_credentials = {
            'username': 'login_user',
            'password': 'lup@ssW@rd'
        }
        self.user = User.objects.create_user(**self.user_credentials)
        self.client.force_login(self.user)
        self.task_data = {'name': '1st'}
        self.task_data_2 = {'name': '2nd'}

    def test_task_authorized(self):
        response = self.client.get(reverse_lazy('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='status/status_list.html')

    def test_task_unathorized(self):
        self.client.logout()
        response = self.client.get(reverse_lazy('task_list'))
        self.assertNotEqual(response.status_code, 302)
        self.assertRedirects(reverse_lazy('home'))

    def test_task_creation(self):
        response = self.client.post(
                reverse_lazy('task_create'),
                data=self.task_data_2,
                )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('status_list'))
        self.assertEqual(len(Task.objects.all()), 2)

    def test_task_deletion(self):
        response = self.client.post(
                reverse_lazy('task_delete', kwargs={'pk': 1})
                )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('task_list'))
        self.assertEqual(len(Task.objects.all()), 0)

    def test_task_update(self):
        response = self.client.post(
                reverse_lazy('task_update', kwargs={'pk': 1}),
                data={'name': 'updated'},
                follow=True
                )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'updated')
