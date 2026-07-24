from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

from .models import Dish, UserProfile, Category
from .forms import DishForm


def home(request):
    query = request.GET.get('q', '')
    category_id = request.GET.get('category', '')

    dishes = Dish.objects.all()

    if query:
        dishes = dishes.filter(title__icontains=query) | dishes.filter(place__icontains=query)

    if category_id:
        dishes = dishes.filter(category_id=category_id)

    categories = Category.objects.all()

    return render(request, 'reviews/home.html', {
        'dishes': dishes,
        'categories': categories,
        'query': query,
        'selected_category': category_id,
    })


def dish_detail(request, pk):
    dish = get_object_or_404(Dish, pk=pk)
    return render(request, 'reviews/dish_detail.html', {'dish': dish})


@login_required(login_url='login')
def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    user_dishes = Dish.objects.filter(author=request.user)

    return render(request, 'reviews/profile.html', {
        'profile': user_profile,
        'dishes': user_dishes
    })


@login_required(login_url='login')
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


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'reviews/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'reviews/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')