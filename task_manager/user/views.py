from django.shortcuts import render
from django.template import context
from django.views import View
from task_manager.user.models import User
from task_manager.user.forms import UserCreationForm


class UserListView(View):

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        return render(
                request,
                'user/index.html',
                context={'users': users},
                )


class UserCreateView(View):
    def get(self, request, *args, **kwargs):
        form = UserCreationForm()
        return render(
                request,
                'user/user.html',
                context={'form': form}
                )

    def post(self, request, *args, **kwargs):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

