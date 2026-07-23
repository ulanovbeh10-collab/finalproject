from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField('Название категории', max_length=100)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Dish(models.Model):
    title = models.CharField('Название блюда', max_length=200)
    place = models.CharField('Заведение / Ресторан', max_length=200)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name='Категория')
    description = models.TextField('Описание и впечатление')
    rating = models.IntegerField('Оценка (от 1 до 5)')
    image = models.ImageField('Фотография блюда', upload_to='dishes/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор обзора')
    created_at = models.DateTimeField('Дата публикации', auto_now_add=True)

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    def __str__(self):
        return f'Профиль {self.user.username}'

    def get_review_count(self):
        return self.user.dish_set.count()