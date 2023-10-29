from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from main.models import *

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl',
        'style': 'background-color: #FDFCF8;'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl',
        'style': 'background-color: #FDFCF8;'
    }))

class SignUpForm(UserCreationForm):
    STATUS_CHOICES = [('M', 'Member'), ('E', 'Employee')]
    status = forms.ChoiceField(
        required=True,
        choices=STATUS_CHOICES,
        widget=forms.Select(attrs={
            'style': 'background-color: #FDFCF8;'
        })
    )
    full_name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl',
        'style': 'background-color: #FDFCF8;'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl',
        'style': 'background-color: #FDFCF8;'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email address',
        'class': 'w-full py-4 px-6 rounded-xl',
        'style': 'background-color: #FDFCF8;'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl',
        'style': 'background-color: #FDFCF8;'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',
        'class': 'w-full py-4 px-6 rounded-xl',
        'style': 'background-color: #FDFCF8;'
    }))
    class Meta:
        model = User
        fields = ('status', 'full_name', 'username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.status = self.cleaned_data["status"]
        user.full_name = self.cleaned_data["full_name"]
        user.email = self.cleaned_data["email"]

        if commit:
            user.save()
        
        return user