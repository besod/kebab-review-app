from django.db import models

# Probably, change User table later in order to save password
# and create user
class User(models.Model):
    user_name = models.CharField(max_length=100, null=False)
    email = models.EmailField(null=False, unique=True)
    password = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name


class Restaurant(models.Model):
    name = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=200, null=False)
    tel = models.IntegerField()
    website = models.URLField()

    def __str__(self):
        return self.name


class Menu(models.Model):
    menu = models.CharField(max_length=100, null=False)
    price = models.IntegerField(null=False)
    description = models.TextField(null=False)
    image = models.ImageField(null=False)
    restaurant_id = models.ForeignKey('core.Restaurant', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    REVIEW_CHOICES = (
        (1, '1 - Bad'),
        (2, '2 - Fair'),
        (3, '3 - Average'),
        (4, '4 - Good'),
        (5, '5 - Excellent'),
    )
    user_id = models.ForeignKey('core.User', on_delete=models.CASCADE)
    menu_id = models.ForeignKey('core.Menu', on_delete=models.CASCADE)
    taste_rating = models.IntegerField(choices=REVIEW_CHOICES, null=False)
    service_rating = models.IntegerField(choices=REVIEW_CHOICES, null=False)
    value_rating = models.IntegerField(choices=REVIEW_CHOICES, null=False)
    total_rating = models.IntegerField()
    slug = models.SlugField(null=False, unique=True)
    like_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


class Contact(models.Model):
    user_name = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=254, null=False, unique=True)
    message = models.TextField(null=False)
    created_at = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.user_name
    

"""
class UserFavoriteRestaurang(models.Model):
    user_id = models.ForeignKey('core.User', on_delete=models.CASCADE)
    review_id = models.ForeignKey('core.Review', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class UserFavoriteReviewer(models.Model):
    user_id = models.ForeignKey('core.User', on_delete=models.CASCADE)
    restaurant_id = models.ForeignKey('core.Restaurant', on_delete=models.CASCADE)
    menu_id = models.ForeignKey('core.Menu', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
"""