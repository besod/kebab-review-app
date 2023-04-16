from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.top, name='top'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('contact/', views.contact, name='contact'),
    path('detail/<int:id>', views.detail, name='detail'),
]
