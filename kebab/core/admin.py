from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Review, Menu, Restaurant


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'username', 'first_name', 'last_name', 'is_staff']

class ReviewAdmin(Review):
    model = Review
    list_display = ['menu_id', 'restaurant_id', 'user_id']

class MenuAdmin(Menu):
    model = Menu
    list_display = ['menu', 'description']

class RestaurantAdmin(Restaurant):
    model = Restaurant
    list_display = ['name']


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Menu)
admin.site.register(Review)
admin.site.register(Restaurant)
