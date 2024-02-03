from django.shortcuts import render
from django.utils.translation import gettext as _
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'
    extra_context = {'title': _('Task Manager')}


class UserLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'user/user_form.html'
    redirect_authenticated_user = True
    next_page = reverse_lazy('home')
    extra_context = {'title': 'Sign in', 'button_text': 'Enter'}


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('home')
