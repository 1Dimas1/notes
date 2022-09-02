from django import forms
from .models import Note
import re
from django.core.exceptions import ValidationError


class NotesFormAdd(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your title here'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 7, 'placeholder': 'Write Content here'}),
            'reminder': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Write a deadline here'}),
            'cat': forms.Select(attrs={'class': 'form-control'})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Title shouldn`t start with number')
        return title


