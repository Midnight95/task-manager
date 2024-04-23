from django.test import TestCase
import json


class LabelTestCase(TestCase):
    fixtures = ['users', 'labels']

    with open('task_manager/fixtures/labels_data.json') as file:
        label_data = json.loads(file.read())
