from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from task_manager.user.models import User
from task_manager.user.forms import UserForm
from django.utils.translation import gettext as _
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import redirect
from task_manager.myxini import DeletionProtectionMixin


class UserPermissionMixin(UserPassesTestMixin):
    def test_func(self):
        if self.request.user != self.get_object():
            self.permission_denied_message = _('You can\'t chage other user!')
            return False
        return True

    def handle_no_permission(self):
        messages.error(self.request, self.get_permission_denied_message())
        return redirect(reverse_lazy('home'))


class UserListView(ListView):
    model = User
    template_name = 'user/user_list.html'
    context_object_name = 'users'
    extra_context = {'title': _('Users')}


class UserCreateView(SuccessMessageMixin, CreateView):
    form_class = UserForm
    template_name = 'forms/form.html'
    extra_context = {
        'title': _('Sign up'),
        'button_text': _('Sign up')
        }
    success_message = _('User created successfully')
    success_url = reverse_lazy('login')


class UserUpdateView(UserPermissionMixin, UpdateView, SuccessMessageMixin):
    model = User
    form_class = UserForm
    template_name = 'forms/form.html'
    extra_context = {
        'title': _('Update user data'),
        'button_text': _('Save changes')
        }
    success_message = _('User updated successfully')
    success_url = reverse_lazy('user_list')


class UserDeleteView(DeletionProtectionMixin, UserPermissionMixin, DeleteView):
    model = User
    template_name = 'forms/delete.html'
    extra_context = {
        'title': _('Delete user data'),
        'button_text': _('Delete user')
    }
    success_url = reverse_lazy('user_list')

    protected_message = _('Looks like this user has some unfinished tasks')
    protected_url = reverse_lazy('user_list')
