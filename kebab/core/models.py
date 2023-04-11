from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(blank=False)
    first_name = None
    last_name = None
    is_superuser = None
    is_staff = None
    is_active = None
    last_login = None

    def __str__(self):
        return self.username


class Restaurant(models.Model):
    name = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=200, null=False)
    tel = models.CharField(max_length=20)
    website = models.URLField()

    def __str__(self):
        return self.name


class Menu(models.Model):
    menu = models.CharField(max_length=100, null=False)
    price = models.IntegerField(null=False)
    description = models.TextField(null=False)
    image = models.ImageField(upload_to='images/', null=False)
    restaurants = models.ManyToManyField(Restaurant)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.menu


class Review(models.Model):
    REVIEW_CHOICES = (
        (1, '1 - Bad'),
        (2, '2 - Fair'),
        (3, '3 - Average'),
        (4, '4 - Good'),
        (5, '5 - Excellent'),
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    taste_rating = models.IntegerField(choices=REVIEW_CHOICES, null=False)
    service_rating = models.IntegerField(choices=REVIEW_CHOICES, null=False)
    value_rating = models.IntegerField(choices=REVIEW_CHOICES, null=False)
    total_rating = models.IntegerField()
    slug = models.SlugField(null=False, unique=True)
    like_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


class Contact(models.Model):
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=254, null=False, unique=True)
    message = models.TextField(null=False)
    created_at = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    

# class FavoriteRestaurant(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='favorite_restaurants')
#     restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='favorited_by')
#     created_at = models.DateTimeField(auto_now_add=True)

# class FavoriteReviewer(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='favorite_reviewers')
#     reviewer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='favorited_by_reviewers')
#     created_at = models.DateTimeField(auto_now_add=True)

# class RestaurantMenu(models.Model):
#     restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='restaurant_menus')
#     menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu_restaurants')
#     created_at = models.DateTimeField(auto_now_add=True)
