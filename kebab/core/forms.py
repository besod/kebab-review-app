from django import forms
from .models import CustomUser, Review, Menu, Restaurant, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate


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


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label='Name',
        widget=forms.TextInput(attrs={
            'class': 'form-input mt-4 block w-full py-3 px-4 rounded-md text-lg bg-white border-gray-400 focus:bg-white focus:outline-none focus:border-blue-500',
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
            'style': 'border: 1px solid #ccc',
            'rows': 4  # Change this value to adjust the height
        }),
        label='Message',
        required=True
    )


class UploadForm(forms.ModelForm):
    taste_rating = forms.IntegerField(
        min_value=1, max_value=10,
        widget=forms.NumberInput(attrs={
            'class': 'form-input mt-4 block w-full py-3 px-4 rounded-md text-lg bg-white border-gray-400 focus:bg-white focus:outline-none focus:border-blue-500',
            'placeholder': 'Score 1-10',
            'style': 'border: 1px solid #ccc'
        })
    )
    service_rating = forms.IntegerField(
        min_value=1, max_value=10,
        widget=forms.NumberInput(attrs={
            'class': 'form-input mt-4 block w-full py-3 px-4 rounded-md text-lg bg-white border-gray-400 focus:bg-white focus:outline-none focus:border-blue-500',
            'placeholder': 'Score 1-10',
            'style': 'border: 1px solid #ccc'
        })
    )
    value_rating = forms.IntegerField(
        min_value=1, max_value=10,
        widget=forms.NumberInput(attrs={
            'class': 'form-input mt-4 block w-full py-3 px-4 rounded-md text-lg bg-white border-gray-400 focus:bg-white focus:outline-none focus:border-blue-500',
            'placeholder': 'Score 1-10',
            'style': 'border: 1px solid #ccc'
        })
    )
    review = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-input mt-4 block w-full py-3 px-4 rounded-md text-lg bg-white border-gray-400 focus:bg-white focus:outline-none focus:border-blue-500',
            'placeholder': 'Please write your review.',
            'style': 'border: 1px solid #ccc'
        })
    )
    image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-input mt-4 block w-full py-3 px-4 rounded-md text-lg bg-white border-gray-400 focus:bg-white focus:outline-none focus:border-blue-500',
            'style': 'border: 1px solid #ccc'
        })
    )
    restaurant_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-input mt-4 block w-full py-3 px-4 rounded-md text-lg bg-white border-gray-400 focus:bg-white focus:outline-none focus:border-blue-500',
            'placeholder': 'ex) Fresh Kebab',
            'style': 'border: 1px solid #ccc'
        })
    )
    restaurant_address = forms.CharField(
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-input mt-4 block w-full py-3 px-4 rounded-md text-lg bg-white border-gray-400 focus:bg-white focus:outline-none focus:border-blue-500',
            'placeholder': 'ex) Stockholm Odenplan 0000',
            'style': 'border: 1px solid #ccc'
        })
    )
    restaurant_tel = forms.CharField(
        max_length=20, required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-input mt-4 block w-full py-3 px-4 rounded-md text-lg bg-white border-gray-400 focus:bg-white focus:outline-none focus:border-blue-500',
            'placeholder': 'ex) 080000000',
            'style': 'border: 1px solid #ccc'
        })
    )
    restaurant_website = forms.URLField(
        required=False,
        widget=forms.URLInput(attrs={
            'class': 'form-input mt-4 block w-full py-3 px-4 rounded-md text-lg bg-white border-gray-400 focus:bg-white focus:outline-none focus:border-blue-500',
            'placeholder': 'https://exmaple.com',
            'style': 'border: 1px solid #ccc'
        })
    )

    menu_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-input mt-4 block w-full py-3 px-4 rounded-md text-lg bg-white border-gray-400 focus:bg-white focus:outline-none focus:border-blue-500',
            'placeholder': 'ex) Chicken kebab',
            'style': 'border: 1px solid #ccc'
        })
    )
    menu_price = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-input mt-4 block w-full py-3 px-4 rounded-md text-lg bg-white border-gray-400 focus:bg-white focus:outline-none focus:border-blue-500',
            'placeholder': 'Price',
            'style': 'border: 1px solid #ccc'
        })
    )

    class Meta:
        model = Review
        exclude = ['user', 'menu', 'restaurant', 'like_count', 'avg_rating']

    def __init__(self, user=None, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        try:
            restaurant = Restaurant.objects.get(
                name=self.cleaned_data['restaurant_name'],
                address=self.cleaned_data['restaurant_address'],
                tel=self.cleaned_data['restaurant_tel'],
                website=self.cleaned_data['restaurant_website']
            )
        except Restaurant.DoesNotExist:
            restaurant = Restaurant.objects.create(
                name=self.cleaned_data['restaurant_name'],
                address=self.cleaned_data['restaurant_address'],
                tel=self.cleaned_data.get('restaurant_tel', ''),
                website=self.cleaned_data.get('restaurant_website', '')
            )

        try:
            menu = Menu.objects.get(
                menu=self.cleaned_data['menu_name'],
                price=self.cleaned_data['menu_price']
            )
        except Menu.DoesNotExist:
            menu = Menu.objects.create(
                menu=self.cleaned_data['menu_name'],
                price=self.cleaned_data['menu_price']
            )
            menu.restaurants.add(restaurant)
            menu.save()

        # Create review
        review = super().save(commit=False)
        if self.user:
            review.user = self.user
        review.restaurant = restaurant
        review.menu = menu

        if commit:
            review.save()
        return review


class CommentForm(forms.ModelForm):
    SERVICE_CHOICES = [(i, str(i)) for i in range(1, 11)]

    name = forms.CharField(
        max_length=80,
        widget=forms.TextInput(attrs={
            'class': 'border-2 border-gray-400 rounded-md py-2 px-3 focus:outline-none focus:ring-2 focus:ring-amber-600 bg-slate-50',
            'placeholder': 'Your username'
        }))
    avg_rating = forms.ChoiceField(
        choices=SERVICE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select mt-4'
                                   }))
    comment = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'border-2 border-gray-400 rounded-md py-2 px-3 focus:outline-none focus:ring-2 focus:ring-amber-600 bg-slate-50',
            'placeholder': 'Leave your comment here.'
        }))

    class Meta:
        model = Comment
        exclude = ['review', 'created_at']


class ReviewForm(forms.ModelForm):
    menu = forms.ModelChoiceField(
        queryset=Menu.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'}),
        empty_label=None,
        to_field_name='name'  # add this to fetch name instead of id
    )
    restaurant = forms.ModelChoiceField(
        queryset=Restaurant.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'}),
        empty_label=None,
        to_field_name='name'  # add this to fetch name instead of id
    )

    class Meta:
        model = Review
        exclude = ['like_count', 'user']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['menu'] = forms.CharField(max_length=255)
        self.fields['restaurant'] = forms.CharField(max_length=255)
