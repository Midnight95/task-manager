from .label_setup import LabelTestCase
from django.urls import reverse_lazy
from task_manager.user.models import User
from task_manager.label.models import Label


class TestLabelCRUD(LabelTestCase):
    def setUp(self):
        user = User.objects.get(pk=1)
        self.client.force_login(user)

    def test_label_page(self):
        response = self.client.get(reverse_lazy('label_list'))
        self.assertEqual(response.label_code, 200)
        self.assertTemplateUsed(
                response, template_name='label/label_list.html'
                )

    def test_label_page_unlogged(self):
        self.client.logout()

        response = self.client.get(reverse_lazy('label_list'))
        self.assertEqual(response.label_code, 302)
        self.assertRedirects(response, reverse_lazy('home'))

    def test_label_creation(self):
        data = self.label_data['valid']
        response = self.client.post(
                reverse_lazy('label_create'),
                data=data,
                )
        self.assertEqual(response.label_code, 302)
        self.assertRedirects(response, reverse_lazy('label_list'))
        self.assertEqual(len(Label.objects.all()), 5)

    def test_label_deletion(self):
        response = self.client.post(
                reverse_lazy('label_delete', kwargs={'pk': 1})
                )
        self.assertEqual(response.label_code, 302)
        self.assertRedirects(response, reverse_lazy('label_list'))
        self.assertEqual(len(Label.objects.all()), 3)

    def test_label_update(self):
        data = self.label_data['valid']
        response = self.client.post(
                reverse_lazy('label_update', kwargs={'pk': 1}),
                data=data,
                follow=True
                )
        self.assertEqual(response.label_code, 200)
        self.assertContains(response, 'updated')
