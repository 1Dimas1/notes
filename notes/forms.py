from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Note
import re


class NotesFormAdd(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'text', 'reminder', 'cat']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write your title here'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 7, 'placeholder': 'Write Content here'}),
            'reminder': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'MM/DD/YYYY'}),
            'cat': forms.Select(attrs={'class': 'form-control'})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Title shouldn`t start with number')
        return title


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
