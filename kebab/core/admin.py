from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Review, Menu, Restaurant


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'username']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ['user_id']

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    model = Menu
    list_display = ['menu', 'description']

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    model = Restaurant
    list_display = ['name']


