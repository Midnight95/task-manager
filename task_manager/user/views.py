from django.shortcuts import render, redirect
from django.urls import reverse
from django.template import context
from django.views import View
from task_manager.user.models import User
from task_manager.user.forms import UserForm


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
        form = UserForm()
        return render(
                request,
                'user/user.html',
                context={'form': form}
                )

    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        return


class UserEditView(View):
    def get(self, request, *args, **kwargs):
        user_id = kwargs['pk']
        user = User.objects.get(id=user_id)
        form = UserForm(instance=user)
        return render(
                request,
                'user/user.html',
                context={'form': form, 'user': user},
                )

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = User.objects.get(id=user_id)
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
        return redirect(reverse('user_list'))
