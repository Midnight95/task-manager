from django.test import TestCase
import json


class TaskTestCase(TestCase):
    fixtures = ['users', 'statuses', 'tasks']

    with open('task_manager/fixtures/tasks_data.json') as file:
        task_test_data = json.loads(file.read())
