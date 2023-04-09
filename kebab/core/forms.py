from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(
        attrs={'class': 'form-input', 'placeholder': 'Username'}
    ))
    email = forms.EmailField(max_length=254, required=True, widget=forms.EmailInput(
        attrs={'class': 'form-input', 'placeholder': 'Email'}
    ))
    password1 = forms.CharField(required=False, widget=forms.PasswordInput(
        attrs={'class': 'form-input', 'placeholder': 'Password'}
    ))
    password2 = forms.CharField(required=False, widget=forms.PasswordInput(
        attrs={'class': 'form-input', 'placeholder': 'Confirm Password'}
    ))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email already exists. Try again!')
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