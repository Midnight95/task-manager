from task_manager.labels.models import Label
from task_manager.labels.forms import LabelForm
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.utils.translation import gettext as _
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.myxini import LoginCheckMixin, DeletionProtectionMixin


class LabelListView(LoginCheckMixin, ListView):
    model = Label
    template_name = 'labels/labels.html'
    context_object_name = 'labels'
    extra_context = {'title': _('Labeles')}


class LabelCreateView(LoginCheckMixin, SuccessMessageMixin, CreateView):
    form_class = LabelForm
    template_name = 'forms/form.html'
    extra_context = {
        'title': _('Create label'),
        'button_text': _('Create')
        }
    success_message = _('Label created successfully')
    success_url = reverse_lazy('labels')


class LabelUpdateView(
        LoginCheckMixin,
        SuccessMessageMixin,
        UpdateView
        ):
    model = Label
    form_class = LabelForm
    template_name = 'forms/form.html'
    extra_context = {
        'title': _('Change label'),
        'button_text': _('Submit'),
    }
    success_message = _('Label updated successfully')
    success_url = reverse_lazy('labels')


class LabelDeleteView(
        DeletionProtectionMixin,
        LoginCheckMixin,
        SuccessMessageMixin,
        DeleteView
        ):
    model = Label
    template_name = 'forms/delete.html'
    success_message = _('Label deleted successfully')
    extra_context = {
            'title': _('Delete label'),
            'button_text': _('Delete label'),
            }
    success_url = reverse_lazy('labels')
    protected_url = success_url
    protected_message = _('Can\t delete linked label')
