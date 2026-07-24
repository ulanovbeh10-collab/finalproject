from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


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
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Категория")
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1, message="Оценка не может быть меньше 1"),
            MaxValueValidator(10, message="Оценка не может быть больше 10")
        ],
        verbose_name="Оценка (1-10)"
    )
    description = models.TextField(blank=True, verbose_name="Описание / Отзыв")
    image = models.ImageField(upload_to='dishes/', blank=True, null=True, verbose_name="Изображение")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.place}"

    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"