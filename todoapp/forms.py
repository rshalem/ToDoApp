from django import forms
from django.forms import TextInput

class ToDoForm(forms.Form):
    task_title = forms.CharField(label='title', max_length=50)
    #widgets = forms.TextInput(attrs={'class': 'form-group', 'placeholder': 'Enter new task'})

