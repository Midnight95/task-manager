from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from task_manager.user.models import User
from task_manager.user.forms import UserForm
from django.utils.translation import gettext as _


class UserListView(ListView):
    model = User
    template_name = 'user/user_list.html'
    context_object_name = 'users'
    extra_context = {'title': _('User list')}


class UserCreateView(CreateView):
    form_class = UserForm 
    template_name = 'user/user.html'
    extra_context = {'title': _('Sign up')}


class UserUpdateView(UpdateView):
    model = User
    fields = '__all__'
    template_name = 'user/user.html'
    extra_context = {'title': _('Edit user data')}
    success_url = reverse_lazy('user_list')


class UserDeleteView(DeleteView):
    model = User
    template_name = 'user/user.html'
    success_url = reverse_lazy('user_list')

