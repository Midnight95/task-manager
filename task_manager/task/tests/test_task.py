from django.urls import reverse_lazy
from task_manager.user.models import User
from task_manager.task.models import Task
from .task_setup import TaskTestCase


class TestTaskCRUD(TaskTestCase):
    def setUp(self):
        self.user = User.objects.get(pk=1)
        self.client.force_login(self.user)

    def test_task_authorized(self):
        response = self.client.get(reverse_lazy('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='task/task_list.html')

    def test_task_unathorized(self):
        self.client.logout()
        response = self.client.get(reverse_lazy('task_list'))
        self.assertNotEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('home'))

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
