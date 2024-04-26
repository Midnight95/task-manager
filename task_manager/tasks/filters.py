import django_filters
from task_manager.tasks.models import Task
from task_manager.statuses.models import Status
from task_manager.users.models import User
from task_manager.labels.models import Label
from django.utils.translation import gettext as _
from django import forms


class TaskFilter(django_filters.FilterSet):

    status = django_filters.ModelChoiceFilter(
        queryset = Status.objects.all(),
        label = _('Status')
    )

    executor = django_filters.ModelChoiceFilter(
        queryset = User.objects.all(),
        label = _('Executor')
    )

    labels = django_filters.ModelChoiceFilter(
        queryset = Label.objects.all(),
        label = _('Label'),
    )

    my_task = django_filters.BooleanFilter(
        method = 'lookup_my_task',
        label = 'Only my tasks',
        widget = forms.CheckboxInput
    )

    def lookup_my_task(self, queryset, name, value):
        lookup = self.request.user
        return queryset.filter(author=lookup)

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels']