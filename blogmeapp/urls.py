from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.signup, name='signup'),
    path('logout/', views.log_out, name='logout'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('home/', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('profile_edit', views.profile_edit, name='profile_edit'),
    path('post_delete/<int:pk>/', views.post_delete, name='post_delete'),
    path('post_edit/<int:pk>/', views.post_edit, name='post_edit'),
]