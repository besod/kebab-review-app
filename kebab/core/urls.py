from django.urls import path
from . import views


urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.top, name='top'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('upload/', views.upload_image, name='upload'),
    path('contact/', views.contact, name='contact'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('profile/<str:username>/', views.user_profile, name='profile'),
    path('review/<int:id>/delete/', views.delete_review, name='delete_review'),
    path('core/review/<int:id>/edit/', views.edit_review, name='edit_review'),
    path('password_change/', views.password_change, name='password_change'),
    path('account_settings/', views.account_settings, name='account_settings'),
    path('search/', views.search_results, name='search_results'),
    path('detail/<int:review_id>/like/', views.like, name='like'),
    path('about/', views.about, name='about'),
]