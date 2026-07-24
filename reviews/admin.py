from django.contrib import admin
from .models import Category, Dish


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'place', 'category', 'rating', 'author', 'created_at')
    list_filter = ('category', 'rating', 'created_at')
    search_fields = ('title', 'place', 'description')