from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from .forms import SignupForm, LogInForm, ContactForm
from .models import Contact, Review, Restaurant, Menu, CustomUser
from django.contrib.auth.decorators import login_required



def home(request):
    context = {}
    context['user'] = CustomUser.objects.all()
    return render(request, 'home.html', context)


# def detail(request, id):
#     context = {}
#     context['review'] = Review.objects.get(id=id)
#     return render(request, 'detail.html', context, status=200)

def detail(request):
    pass


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignupForm()
    return render(request, 'account/signup.html', {'form': form})


@login_required(login_url='login')
def userpage(request):
    pass


def log_in(request):
    error = False
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        form = LogInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                error = True
    else:
        form = LogInForm()

    return render(request, 'account/login.html', {'form': form, 'error': error})


def log_out(request):
    logout(request)
    return redirect(reverse('account:login'))


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
        return render(request, 'contact.html', context)


# When inplement create_review function, use this maybe
# reviews = Review.objects.filter(restaurant=restaurant)
    # average_rating = reviews.aggregate(Avg('rating'))['rating__avg']