from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('userpage/', views.userpage, name='userpage'),
    path('detail/', views.detail, name='detail'),
    path('contact/', views.contact, name='contact'),
]
