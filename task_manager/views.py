from django.shortcuts import render
from django.views import View
from django.utils.translation import gettext as _

class IndexView(View):

    def get(self, request, *args, **kwargs):
        welcome_msg = _("Task manager! Enjoy!")
        return render(
            request,
            "index.html",
            context = {"welcome_msg": welcome_msg},
        )
