from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Dish(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название блюда")
    place = models.CharField(max_length=200, verbose_name="Заведение")
    description = models.TextField(blank=True, verbose_name="Описание")
    rating = models.IntegerField(default=5, verbose_name="Оценка (1-10)")
    image = models.ImageField(upload_to='dishes/', blank=True, null=True, verbose_name="Картинка")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Категория")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dishes', verbose_name="Автор")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    def __str__(self):
        return f"{self.title} ({self.place})"

    class Meta:
        verbose_name = "Обзор блюда"
        verbose_name_plural = "Обзоры блюд"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name="Аватар")
    bio = models.TextField(blank=True, verbose_name="О себе")

    def __str__(self):
        return f"Профиль {self.user.username}"