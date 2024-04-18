from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _


class LoginCheckMixin(LoginRequiredMixin):
    login_url = reverse_lazy('home')
    redirect_field_name = None
    permission_denied_message = _('You must log in to view this page')
