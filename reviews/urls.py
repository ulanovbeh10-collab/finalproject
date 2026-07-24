from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dish/<int:pk>/', views.dish_detail, name='dish_detail'),
    path('dish/add/', views.add_dish, name='add_dish'),
    path('dish/<int:pk>/edit/', views.edit_dish, name='edit_dish'),
    path('dish/<int:pk>/delete/', views.delete_dish, name='delete_dish'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]