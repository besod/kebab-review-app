from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import SignupForm, LoginForm, ContactForm
from .models import Contact
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'core/index.html', {}, status=200)

def login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user:
                login(request, user)
                return redirect('/userpage/')
    else:
        form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'core/login.html', context, status=200)

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            # CustomUser.objects.create(
            #     username = form.cleaned_data['username'],
            #     email = form.cleaned_data['email'],
            #     password = form.cleaned_data['password'],
            # )
            return render(request, 'core/userpage.html', status=200)
    else:
        form = SignupForm()
    context = {
        'form': form
    }
    return render(request, 'core/signup.html', context, status=200)

def logout(request):
    pass

@login_required(login_url='core/login.html')
def userpage(request):
    pass

@login_required(login_url='core/login.html')
def detail(request):
    pass

def contact(request):
    context = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            Contact.objects.create(
                name = form.cleaned_data['name'],
                email = form.cleaned_data['email'],
                title = form.cleaned_data['title'],
                message = form.cleaned_data['message']
            )
        context = {
            'form': form,
        }
    else:
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, 'core/contact.html', context, status=200)
