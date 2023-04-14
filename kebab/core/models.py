from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.db import models



class CustomUserManager(BaseUserManager):

    # Create two methods: create_user and create_superuser
    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        # One application of normalizing emails is to prevent multiple signups
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(
                "Superuser must have is_staff=True."
            )
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(
                "Superuser must have is_superuser=True."
            )

        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    # we have to wait at least until this step to run the migrations (until we create our own user model).
    # The REQUIRED_FIELDS should be equal to ['username'] because this variable represents field names that will
    # be prompted for when creating a user via the createsuperuser management command.
    
    # first_name = None
    # last_name = None
    # is_superuser = None
    # is_staff = None
    # is_active = None
    email = models.EmailField("email address", unique=True, blank=False)

    USERNAME_FIELD = "email"  # make the user log in with the email
    REQUIRED_FIELDS = ["username"]

    objects = CustomUserManager()

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
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name='reviews_by_user'
    )
    menu = models.ForeignKey(
        Menu, on_delete=models.CASCADE, related_name='reviews_of_menu'
    )
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name='restaurants_for_review'
    )
    taste_rating = models.IntegerField(choices=REVIEW_CHOICES, null=False)
    service_rating = models.IntegerField(choices=REVIEW_CHOICES, null=False)
    value_rating = models.IntegerField(choices=REVIEW_CHOICES, null=False)
    total_rating = models.IntegerField()
    slug = models.SlugField(null=False, unique=True)
    like_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)


class Contact(models.Model):
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=254, null=False, unique=True)
    message = models.TextField(null=False)
    created_at = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    

# Use Django's default function to create user
# class CustomUser(AbstractUser):
#     email = models.EmailField(blank=False)
#     first_name = None
#     last_name = None
#     is_superuser = None
#     is_staff = None
#     is_active = None
#     last_login = None

#     def __str__(self):
#         return self.username


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

# Define custom manager that extends BaseUserManager.We make email field unique to be
# able to use it as the unique identifier.

