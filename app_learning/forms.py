from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        widgets = {'text': forms.Textarea(attrs={'cols':80})}
    
    def get_initial(self):
        initial = super().get_initial()
        initial['user'] = self.user_id
        return initial
