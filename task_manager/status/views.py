from django.shortcuts import render
from django.views.generic.list import ListView
from task_manager.status.models import Status

class StatusListView(ListView):
    model = Status


class StatusCreateView():
    pass


class StatusUpdateView():
    pass


class StatusDeleteView():
    pass