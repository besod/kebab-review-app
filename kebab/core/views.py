from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import SignupForm, ContactForm
from .models import Contact
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index(request):
    return render(request, 'core/index.html', {}, status=200)

def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login succeeded')
            return redirect('userpage')
        else:
            messages.error(request, 'Invalid password or email address. Try again')
    return render(request, 'accounts/login.html', status=200)


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # CustomUser.objects.create(
            #     username = form.cleaned_data['username'],
            #     email = form.cleaned_data['email'],
            #     password = form.cleaned_data['password'],
            # )
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form':form}, status=200)


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def userpage(request):
    pass


@login_required
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
