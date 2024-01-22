from django.shortcuts import render
from django.views import View
from django.utils.translation import gettext as _
from django.contrib.auth.views import LoginView
from task_manager.user.models import User
from django.urls import reverse_lazy

class IndexView(View):
    def get(self, request, *args, **kwargs):
        welcome_msg = _("Task manager! Enjoy!")
        return render(
            request,
            "index.html",
            context = {"welcome_msg": welcome_msg},
        )


class UserLoginView(LoginView):
    model =  User
    template_name = 'user/user_form.html'
    redirect_authenticated_user = True
    next_page = reverse_lazy('home')
    extra_context = {'title': 'Sign in', 'button_text': 'Enter'}
