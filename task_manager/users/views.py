from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from task_manager.users.models import User
from task_manager.users.forms import UserForm, UserUpdateForm
from django.utils.translation import gettext as _
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import redirect
from task_manager.mixins import DeletionProtectionMixin


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
    template_name = 'users/users.html'
    context_object_name = 'users'


class UserCreateView(SuccessMessageMixin, CreateView):
    form_class = UserForm
    template_name = 'users/user_sign_up_form.html'
    success_message = _('User created successfully')
    success_url = reverse_lazy('login')


class UserUpdateView(SuccessMessageMixin, UserPermissionMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'users/user_update_form.html'
    success_message = _('User updated successfully')
    success_url = reverse_lazy('users')


class UserDeleteView(SuccessMessageMixin, DeletionProtectionMixin, UserPermissionMixin, DeleteView):
    model = User
    template_name = 'users/user_delete.html'
    success_url = reverse_lazy('users')
    success_message = _('User deleted successfully')

    protected_message = _('Looks like this user has some unfinished tasks')
    protected_url = reverse_lazy('users')
