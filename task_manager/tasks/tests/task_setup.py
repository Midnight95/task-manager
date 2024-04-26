from django.test import TestCase, modify_settings
import json


@modify_settings(
    MIDDLEWARE={
        'remove': 'rollbar.contrib.django.middleware.RollbarNotifierMiddleware',
    }
)
class TaskTestCase(TestCase):
    fixtures = ['users', 'statuses', 'tasks']

    with open('task_manager/fixtures/tasks_data.json') as file:
        task_test_data = json.loads(file.read())
