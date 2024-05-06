from .status_setup import StatusTestCase
from django.urls import reverse_lazy
from task_manager.users.models import User
from task_manager.statuses.models import Status


class TestStatusCRUD(StatusTestCase):
    def setUp(self):
        user = User.objects.get(pk=1)
        self.client.force_login(user)

    def test_status_page(self):
        response = self.client.get(reverse_lazy('statuses'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
                response, template_name='statuses/statuses.html'
                )

    def test_status_page_unlogged(self):
        self.client.logout()

        response = self.client.get(reverse_lazy('statuses'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('home'))

    def test_status_creation(self):
        data = self.status_data['valid']
        response = self.client.post(
                reverse_lazy('status_create'),
                data=data,
                )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('statuses'))
        self.assertEqual(len(Status.objects.all()), 5)

    def test_status_deletion(self):
        response = self.client.post(
                reverse_lazy('status_delete', kwargs={'pk': 1})
                )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('statuses'))
        self.assertEqual(len(Status.objects.all()), 3)

    def test_status_update(self):
        data = self.status_data['valid']
        response = self.client.post(
                reverse_lazy('status_update', kwargs={'pk': 1}),
                data=data,
                follow=True
                )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, data['name'])
