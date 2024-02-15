from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from task_manager.user.models import User
from task_manager.user.forms import UserForm
from django.utils.translation import gettext as _
from django.contrib.auth.mixins import LoginRequiredMixin
from task_manager.myxini import PermissionCheckMixin


class UserListView(ListView):
    model = User
    template_name = 'user/user_list.html'
    context_object_name = 'users'
    extra_context = {'title': _('User list')}


class UserCreateView(CreateView):
    form_class = UserForm
    template_name = 'user/user_form.html'
    extra_context = {'title': _('Sign up'), 'button_text': _('Sign up')}
    success_url = reverse_lazy('login')


class UserUpdateView(UpdateView, LoginRequiredMixin, PermissionCheckMixin):
    model = User
    form_class = UserForm
    template_name = 'user/user_form.html'
    extra_context = {'title': _('Update user data'), 'button_text': _('Save changes')}
    success_url = reverse_lazy('user_list')


class UserDeleteView(DeleteView, LoginRequiredMixin, PermissionCheckMixin):
    model = User
    template_name = 'user/delete_user.html'
    extra_context = {
        'title': _('Delete user data'),
        'button_text': _('Are you sure you want to?')
    }
    success_url = reverse_lazy('user_list')
