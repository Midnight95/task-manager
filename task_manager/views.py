from django.utils.translation import gettext as _
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.base import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


class IndexView(TemplateView):
    template_name = 'index.html'
    extra_context = {'title': _('Task Manager')}


class UserLoginView(SuccessMessageMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'user/user_form.html'
    redirect_authenticated_user = True
    next_page = reverse_lazy('home')
    extra_context = {'title': 'Sign in', 'button_text': 'Enter'}
    success_message = _('You have logged in!')


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, _('You are logged out.'))
        return super().dispatch(request, *args, **kwargs)
