from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dish/<int:pk>/', views.dish_detail, name='dish_detail'),
    path('profile/', views.profile, name='profile'),
    path('add/', views.add_dish, name='add_dish'),
]