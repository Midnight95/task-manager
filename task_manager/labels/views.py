from task_manager.labels.models import Label
from task_manager.labels.forms import LabelForm
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.utils.translation import gettext as _
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from task_manager.mixins import LoginCheckMixin, DeletionProtectionMixin


class LabelListView(LoginCheckMixin, ListView):
    model = Label
    template_name = 'labels/labels.html'
    context_object_name = 'labels'


class LabelCreateView(LoginCheckMixin, SuccessMessageMixin, CreateView):
    form_class = LabelForm
    template_name = 'labels/label_create_form.html'
    success_message = _('Label created successfully')
    success_url = reverse_lazy('labels')


class LabelUpdateView(
        LoginCheckMixin,
        SuccessMessageMixin,
        UpdateView
        ):
    model = Label
    form_class = LabelForm
    template_name = 'labels/label_update_form.html'
    success_message = _('Label updated successfully')
    success_url = reverse_lazy('labels')


class LabelDeleteView(
        DeletionProtectionMixin,
        LoginCheckMixin,
        SuccessMessageMixin,
        DeleteView
        ):
    model = Label
    template_name = 'labels/label_delete_form.html'
    success_message = _('Label deleted successfully')
    success_url = reverse_lazy('labels')
    protected_url = success_url
    protected_message = _('Can\t delete linked label')
