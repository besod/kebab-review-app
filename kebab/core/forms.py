from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    pass


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label='First name',
        widget=forms.TextInput(attrs={'class': 'w-full mb-1'}),
        required=True
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'w-full mb-1'}),
        required=True
    )
    title = forms.CharField(
        label='Title',
        widget=forms.TextInput(attrs={'class': 'w-full mb-1'}),
        required=True
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'w-full mb-1'}),
        label='Message',
        required=True
    )