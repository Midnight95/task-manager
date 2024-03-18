from task_manager.status.models import Status
from task_manager.status.forms import StatusForm
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic.list import ListView
from django.utils.translation import gettext as _
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class StatusListView(ListView):
    model = Status
    template_name = 'status/status_list.html'
    context_object_name = 'statuses'
    extra_context = {'title': _('Statuses')}


class StatusCreateView(CreateView):
    form_class = StatusForm
    template_name = 'form/form.html'
    extra_context = {'title': _('Create status'), 'button_text': _('Create')}
    success_url = reverse_lazy('status_list')


class StatusUpdateView(UpdateView):
    model = Status
    form_class = StatusForm
    


class StatusDeleteView():
    pass