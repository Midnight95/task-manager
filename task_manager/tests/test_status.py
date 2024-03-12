from django.test import TestCase
from django.urls import reverse_lazy
from task_manager.user.models import User
from task_manager.status.models import Status


class TestStatus(TestCase):
    def setUp(self):
        self.user_credentials = {
            'username': 'login_user',
            'password': 'lup@ssW@rd'
        }
        self.user = User.objects.create_user(**self.user_credentials)
        self.client.force_login(self.user)

    def test_status_page(self):
        response = self.client.get(reverse_lazy('status_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTempateUsed(response, tempate_name='status/statuses.html')

    def test_status_creation(self):
        pass
