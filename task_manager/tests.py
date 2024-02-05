from django.test import TestCase, Client
from django.urls import reverse_lazy
from task_manager.user.models import User


class TestMixin(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.credentials = {
            'username': 'user',
            'password': 'ASFD&l098877'
        }

        cls.user = User.objects.create(**cls.credentials)


class TestIndex(TestMixin):
    def test_index_view(self):
        response = self.client.get(reverse_lazy('home'))

        self.assertEqual(response.status_code, 200) 
