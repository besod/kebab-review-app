from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class SignupForm(UserCreationForm):
    username = forms.CharField(
        max_length=100, required=True, widget=forms.TextInput(
        attrs={'class': 'form-input mb-1'})
    )
    email = forms.EmailField(
        max_length=254, required=True, widget=forms.EmailInput(
        attrs={'class': 'form-input mb-1'})
    )
    password1 = forms.CharField(
        required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-input mb-1'})
    )
    password2 = forms.CharField(
        required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-input'})
    )
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError('This username already exist.')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('This email already exists.')
        return email


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