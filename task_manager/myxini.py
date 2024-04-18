from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.contrib import messages


class LoginCheckMixin(LoginRequiredMixin):
    login_url = reverse_lazy('home')
    redirect_field_name = None
    permission_denied_message = _('You must log in to view this page')

    def handle_no_permission(self):
        messages.error(self.request, self.get_permission_denied_message())
        return redirect(self.login_url)