from django.test import TestCase, Client
from django.urls import reverse_lazy
from task_manager.user.models import User


class TestMixin(TestCase):
    def setUp(self):
        self.client = Client()
        self.credentials = {
            'username': 'user',
            'password': 'ASFD&l098877'
        }

        self.user = User.objects.create(**self.credentials)


class TestIndex(TestMixin):
    def test_index_view(self):
        response = self.client.get(reverse_lazy('home'))

        assert response.status_code == 200