from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth import authenticate


class HomeForm(forms.Form):
    pass


class SignupForm(UserCreationForm):
    username = forms.CharField(
        max_length=100, required=True, widget=forms.TextInput(
            attrs={
                    'class': 'form-input mt-4 mb-4 block w-full py-3 px-4 rounded-md text-lg bg-white border-gray-900 focus:bg-white focus:outline-none focus:border-blue-500',
                    'placeholder': 'Username',
                    'style': 'border: 1px solid #ccc',
                    'autocomplete': 'off'
            }
        )
    )
    email = forms.EmailField(
        max_length=254, required=True, widget=forms.EmailInput(
            attrs={
                    'class': 'form-input mt-4 mb-4 block w-full py-3 px-4 rounded-md text-lg bg-white border-gray-900 focus:bg-white focus:outline-none focus:border-blue-500',
                    'placeholder': 'Email',
                    'style': 'border: 1px solid #ccc',
                    'autocomplete': 'off'
            }
        )
    )
    password1 = forms.CharField(
        label='Password', required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-input mt-4 mb-4 block w-full py-3 px-4 rounded-md text-lg bg-white border-gray-900 focus:bg-white focus:outline-none focus:border-blue-500',
                'placeholder': 'Password',
                'style': 'border: 1px solid #ccc',
            }
        )
    )
    password2 = forms.CharField(
        label='Password confirmation', required=True,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-input mt-4 mb-4 block w-full py-3 px-4 rounded-md text-lg bg-white border-gray-900 focus:bg-white focus:outline-none focus:border-blue-500',
                'placeholder': 'Password confirmation',
                'style': 'border: 1px solid #ccc',
            }
        )
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


class LogInForm(forms.Form):

    email = forms.EmailField(required=True,
                             widget=forms.EmailInput(attrs={
                                 'class': 'form-input mt-4 mb-4 block w-full py-3 px-4 rounded-md text-lg bg-white border-gray-900 focus:bg-white focus:outline-none focus:border-blue-500',
                                 'placeholder': 'Email',
                                 'style': 'border: 1px solid #ccc',
                                 'autocomplete': 'off'
                             }))
    password = forms.CharField(required=True,
                               widget=forms.PasswordInput(attrs={
                                   'class': 'form-input mt-4 block w-full py-3 px-4 rounded-md text-lg bg-white border-gray-400 focus:bg-white focus:outline-none focus:border-blue-500',
                                   'placeholder': 'Password',
                                   'style': 'border: 1px solid #ccc'
                               }))
    remember_me = forms.BooleanField(
        required=False, initial=False, widget=forms.CheckboxInput(attrs={
            'class': 'form-checkbox text-blue-500 mr-2',
            'id': 'remember-me'
        }))
    # def clean(self, *args, **kwargs):
    #     email = self.cleaned_data.get('email')
    #     password = self.cleaned_data.get('password')

    #     if email and password:
    #         user = authenticate(email=email, password=password)

    #         if not user:
    #             raise forms.ValidationError('user does not exist')

    #         if not user.check_password(password):
    #             raise forms.ValidationError('incorrect password')

    #     return super(LogInForm, self).clean(*args, **kwargs)


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label='Name',
        widget=forms.TextInput(attrs={
                                'class': 'form-input mt-4 block w-full py-3 px-4 rounded-md text-lgbg-white border-gray-400 focus:bg-white focus:outline-none focus:border-blue-500',
                                'placeholder': 'Name',
                                'style': 'border: 1px solid #ccc'
        }),
        required=True
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={
                                'class': 'form-input mt-4 block w-full py-3 px-4 rounded-md text-lg bg-white border-gray-400 focus:bg-white focus:outline-none focus:border-blue-500',
                                'placeholder': 'Email',
                                'style': 'border: 1px solid #ccc'
        }),
        required=True
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
                                'class': 'form-input mt-4 block w-full py-3 px-4 rounded-md text-lg bg-white border-gray-400 focus:bg-white focus:outline-none focus:border-blue-500',
                                'placeholder': 'Message',
                                'style': 'border: 1px solid #ccc'
        }),
        label='Message',
        required=True
    )