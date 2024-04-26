from django.test import TestCase, modify_settings
from django.urls import reverse_lazy


@modify_settings(
    MIDDLEWARE={
        'remove': 'rollbar.contrib.django.middleware.RollbarNotifierMiddleware',
    }
)
class TestIndex(TestCase):
    def setUp(self):
        self.response = self.client.get(reverse_lazy('home'))

    def test_index_view(self):

        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, template_name='index.html')
        self.assertContains(self.response, 'Task Manager')

        self.assertContains(self.response, '/users/')
        self.assertContains(self.response, '/users/create/')
        self.assertContains(self.response, '/login/')
        self.assertNotContains(self.response, '/logout/')
