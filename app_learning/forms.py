from django import forms
from .models import Topic

class TopicForm(forms.ModelForm):
    model = Topic
    fields = ['text']