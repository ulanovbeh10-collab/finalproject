from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dish/<int:pk>/', views.dish_detail, name='dish_detail'),
    path('dish/<int:pk>/edit/', views.edit_dish, name='edit_dish'),
    path('dish/<int:pk>/delete/', views.delete_dish, name='delete_dish'),
    path('dish/add/', views.add_dish, name='add_dish'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]