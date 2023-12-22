# forms.py

from django import forms
from .models import tasktable

class TaskForm(forms.ModelForm):
    class Meta:
        model = tasktable
        exclude = ['id']  # Exclude the 'id' field from the form
