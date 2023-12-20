from django.forms import ModelForm
from task_manager.user.models import User


class UserCreationForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'username', 'password']


