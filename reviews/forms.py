from django import forms
from .models import Dish


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['title', 'place', 'category', 'rating', 'description', 'image']
        labels = {
            'title': 'Название блюда',
            'place': 'Заведение',
            'category': 'Категория',
            'rating': 'Оценка (от 1 до 10)',
            'description': 'Описание / Отзыв',
            'image': 'Изображение',
        }