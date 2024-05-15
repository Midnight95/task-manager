from task_manager.statuses.models import Status
from task_manager.statuses.forms import StatusForm
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.utils.translation import gettext as _
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import LoginCheckMixin, DeletionProtectionMixin


class StatusListView(LoginCheckMixin, ListView):
    model = Status
    template_name = 'statuses/statuses.html'
    context_object_name = 'statuses'
    extra_context = {'title': _('Statuses')}


class StatusCreateView(LoginCheckMixin, SuccessMessageMixin, CreateView):
    form_class = StatusForm
    template_name = 'statuses/status_create_form.html'
    success_message = _('Status created successfully')
    success_url = reverse_lazy('statuses')


class StatusUpdateView(
        LoginCheckMixin,
        SuccessMessageMixin,
        UpdateView
        ):
    model = Status
    form_class = StatusForm
    template_name = 'forms/form.html'
    success_message = _('Status updated successfully')
    success_url = reverse_lazy('statuses')


class StatusDeleteView(
        DeletionProtectionMixin,
        LoginCheckMixin,
        SuccessMessageMixin,
        DeleteView
        ):
    model = Status
    template_name = 'statuses/status_delete_form.html'
    success_message = _('Status deleted successfully')
    success_url = reverse_lazy('statuses')
    protected_url = success_url
    protected_message = _('Can\t delete linked status')
