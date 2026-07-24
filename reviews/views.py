from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.db.models import Q
from .models import Dish, Category
from .forms import DishForm


# Главная страница
def home(request):
    query = request.GET.get('q', '')
    category_id = request.GET.get('category', '')

    dishes = Dish.objects.all().order_by('-created_at')

    if query:
        dishes = dishes.filter(
            Q(title__icontains=query) | Q(place__icontains=query)
        )

    if category_id:
        dishes = dishes.filter(category_id=category_id)

    categories = Category.objects.all()

    context = {
        'dishes': dishes,
        'categories': categories,
        'query': query,
        'selected_category': category_id,
    }
    return render(request, 'reviews/home.html', context)


# Детальный просмотр блюда
def dish_detail(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    return render(request, 'reviews/dish_detail.html', {'dish': dish})


# Добавление нового обзора
@login_required
def add_dish(request):
    if request.method == 'POST':
        form = DishForm(request.POST, request.FILES)
        if form.is_valid():
            dish = form.save(commit=False)
            dish.author = request.user
            dish.save()
            return redirect('home')
    else:
        form = DishForm()
    return render(request, 'reviews/add_dish.html', {'form': form})


# Редактирование обзора (только для автора)
@login_required
def edit_dish(request, pk):
    dish = get_object_or_404(Dish, pk=pk, author=request.user)
    if request.method == 'POST':
        form = DishForm(request.POST, request.FILES, instance=dish)
        if form.is_valid():
            form.save()
            return redirect('dish_detail', pk=dish.pk)
    else:
        form = DishForm(instance=dish)
    return render(request, 'reviews/edit_dish.html', {'form': form, 'dish': dish})


# Удаление обзора (только для автора)
@login_required
def delete_dish(request, pk):
    dish = get_object_or_404(Dish, pk=pk, author=request.user)
    if request.method == 'POST':
        dish.delete()
        return redirect('home')
    return render(request, 'reviews/delete_dish.html', {'dish': dish})


# Регистрация пользователя
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


# Профиль пользователя
@login_required
def profile(request):
    user_dishes = Dish.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'reviews/profile.html', {'dishes': user_dishes})