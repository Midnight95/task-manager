from django.test import TestCase
import json


class TaskTestCase(TestCase):
    fixtures = ['user_objects', 'status_objects', 'task_objects']

    with open('task_manager/fixtures/task_test_data.json') as file:
        status_data = json.loads(file.read())