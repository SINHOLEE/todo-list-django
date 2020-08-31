from .models import Todo
from django.forms import ModelForm

class TodoCreateForm(ModelForm):
    class Meta:
        model=Todo
        fields = ['content',]

