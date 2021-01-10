from django import forms

class TaskForm(forms.Form):
    task_name = forms.CharField(max_length=200)
    task_description = forms.CharField(max_length=2000)