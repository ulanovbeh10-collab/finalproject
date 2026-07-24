from django import forms
from .models import Dish


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['title', 'place', 'category', 'rating', 'description', 'image']
        widgets = {
            'rating': forms.NumberInput(attrs={
                'min': 1,
                'max': 10,
                'placeholder': 'От 1 до 10'
            }),
        }
        labels = {
            'title': 'Название блюда',
            'place': 'Заведение',
            'category': 'Категория',
            'rating': 'Оценка (1-10)',
            'description': 'Описание / Отзыв',
            'image': 'Изображение',
        }