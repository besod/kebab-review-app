from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from .forms import SignupForm, LogInForm, ContactForm, UploadForm, CommentForm
from .models import Contact, Review, CustomUser, Comment
from django.contrib.auth.decorators import login_required


# def home(request):
# context = {}
# context['user'] = CustomUser.objects.all()
# return render(request, 'core/home.html', context)


def top(request):
    sort = request.GET.get('sort-by', '-created_at')
    restaurant_name = request.GET.get('restaurant')
    menu_name = request.GET.get('menu')
    reviewer_name = request.GET.get('reviewer')

    reviews = Review.objects.all()
    best = Review.objects.order_by(
        'menu__price', '-avg_rating', '-like_count', '-created_at').first()
    # Get distinct restaurant names
    restaurants = Review.objects.order_by().values_list(
        'restaurant__name', flat=True).distinct()
    # Get distinct menu names
    menus = Review.objects.order_by().values_list(
        'menu__menu', flat=True).distinct()
    # Get distinct reviewer names
    reviewers = Review.objects.order_by().values_list(
        'user__username', flat=True).distinct()

    if restaurant_name:
        reviews = reviews.filter(restaurant__name=restaurant_name)
    elif menu_name:
        reviews = reviews.filter(menu__menu=menu_name)
    elif reviewer_name:
        reviews = reviews.filter(user__username=reviewer_name)

    if sort:
        reviews = reviews.order_by(sort)

    context = {
        'reviews': reviews,
        'best': best,
        'restaurants': restaurants,
        'menus': menus,
        'reviewers': reviewers
    }
    return render(request, 'core/top.html', context)


def detail(request, id):
    review = get_object_or_404(Review, id=id)
    context = {
        'review': review
    }
    return render(request, 'core/detail.html', context, status=200)


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('core:top')
    else:
        form = SignupForm()
    return render(request, 'account/signup.html', {'form': form})


def log_in(request):
    error = False
    if request.user.is_authenticated:
        return redirect('/core/')
    if request.method == "POST":
        form = LogInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                return redirect('/core/')
            else:
                error = True
    else:
        form = LogInForm()

    return render(request, 'account/login.html', {'form': form, 'error': error})


@login_required
def upload_image(request):
    if request.method == 'POST':
        # request.POST, request.FILES
        form = UploadForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            # messages.success(request, 'Image added successfully')
            form.save_m2m()  # Save many-to-many relationships
            return redirect('core:top')
    else:
        form = UploadForm(data=request.GET)

    return render(request, 'account/upload.html', {'form': form})


def log_out(request):
    logout(request)
    return redirect(reverse('core:top'))


def contact(request):
    context = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            Contact.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
        return redirect('/core/')
    else:
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, 'core/contact.html', context)


def user_profile(request, username):
    context = {}
    user = get_object_or_404(CustomUser, username=username)
    context = {
        'user': user
    }
    redirect
    return render(request, 'account/profile.html', context=context)


def post_comment(request, id):
    review = get_object_or_404(Review, id=id)
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.review = review
        comment.save()
    context = {
        'target_review': review,
        'comment_form': form,
        'comment': comment
    }
    return render(request, 'core/detail.html', context)



# When inplement create_review function, use this maybe
# reviews = Review.objects.filter(restaurant=restaurant)
    # average_rating = reviews.aggregate(Avg('rating'))['rating__avg']
