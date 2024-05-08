from task_manager.users.models import User
from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
                'username',
                'first_name',
                'last_name',
                'password1',
                'password2'
                ]


class UserUpdateForm(UserForm):
    def clean_username(self):
        username = self.cleaned_data.get('username')

        return username
