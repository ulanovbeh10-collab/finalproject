from django.contrib import admin
from .models import Category, Dish, UserProfile


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'place', 'category', 'rating', 'author', 'created_at')
    list_display_links = ('id', 'title')
    list_filter = ('category', 'rating', 'created_at')
    search_fields = ('title', 'place', 'description')


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')