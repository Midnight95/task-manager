from task_manager.status.models import Status
from task_manager.status.forms import StatusForm
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.utils.translation import gettext as _
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin


class StatusListView(ListView):
    model = Status
    template_name = 'status/status_list.html'
    context_object_name = 'statuses'
    extra_context = {'title': _('Statuses')}


class StatusCreateView(SuccessMessageMixin, CreateView):
    form_class = StatusForm
    template_name = 'forms/form.html'
    extra_context = {
        'title': _('Create status'),
        'button_text': _('Create')
        }
    success_url = reverse_lazy('status_list')


class StatusUpdateView(SuccessMessageMixin, UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'forms/form.html'
    extra_context = {
        'title': _('Change status'),
        'button_text': _('Submit'),
    }
    success_message = _('Status updated successfully')
    success_url = reverse_lazy('status_list')


class StatusDeleteView(SuccessMessageMixin, DeleteView):
    model = Status
    template_name = 'forms/delete.form'
    success_message = _('Status deleted successfully')
    extra_context = {
            'title': _('Delete status'),
            'button_text': _('Delete status'),
            }
    success_url = reverse_lazy('status_list')
