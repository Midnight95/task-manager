from task_manager.status.models import Status
from django import forms


class StatusForm(forms.ModelForm):
    name = forms.CharField(max_length=100)

    class Meta:
        model = Status
        fields = ['name']

