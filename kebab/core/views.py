from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from .forms import SignupForm, LogInForm, ContactForm, UploadForm, CommentForm, ReviewForm
from .models import Contact, Review, CustomUser, Comment
from django.contrib.auth.decorators import login_required
from django.http import Http404, JsonResponse, HttpResponseBadRequest

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
    target_review = get_object_or_404(Review, id=id)
    comments = Comment.objects.filter(review=target_review)
    if comments:
        total = 0
        for comment in comments.values():
            total += comment['avg_rating']
        viewer_avg_rating = round(total/comments.count(), 1)
    else:
        viewer_avg_rating = 'Nothing'

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.review = target_review
            comment.save()
            return redirect('core:detail', id=id)
    else:
        form = CommentForm()

    context = {
        'review': target_review,
        'comment_form': form,
        'comments': comments,
        'viewer_rating': viewer_avg_rating
    }
    return render(request, 'core/detail.html', context)


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


@login_required
def user_profile(request, username):
    user = get_object_or_404(CustomUser, username=username)
    reviews = Review.objects.filter(user=user)
    context = {'user': user, 'reviews': reviews}
    return render(request, 'account/profile.html', context)


@login_required
def delete_review(request, id):
    review = get_object_or_404(Review, id=id)
    if request.method == 'POST':
        # Delete the review from the database
        review.delete()
        # Redirect the user to the home page
        return redirect('core:top')
    return render(request, 'core/delete_review.html', {'review': review})


@login_required
def edit_review(request, id):
    review = get_object_or_404(Review, id=id, user=request.user)
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            return redirect('core:profile', username=request.user.username)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'core/edit_review.html', {'form': form})


@login_required
def password_change(request):
    # add password change functionality
    return render(request, 'account/password_change.html')


@login_required
def account_settings(request):
    # Add account settings functionality
    return render(request, 'account/account_settings.html')


def like(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    review.like_count +=1
    review.save()
    return JsonResponse({"review_like_count": review.like_count})




# When inplement create_review function, use this maybe
# reviews = Review.objects.filter(restaurant=restaurant)
    # average_rating = reviews.aggregate(Avg('rating'))['rating__avg']
