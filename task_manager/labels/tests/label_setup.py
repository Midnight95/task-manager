from django.test import TestCase
import json


class LabelTestCase(TestCase):
    fixtures = ['user_objects', 'label_objects']

    with open('task_manager/fixtures/label_test_data.json') as file:
        status_data = json.loads(file.read())
