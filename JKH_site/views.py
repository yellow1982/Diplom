from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import Category


def registration(request):
    if request.method == 'POST':
        form = NewUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('JKH_site:home_page')
    else:
        form = NewUserCreationForm()
    return render(request, 'JKH_site/registration.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('JKH_site:home_page')
    else:
        form = LoginForm()
    return render(request, 'JKH_site/login.html', {'form': form})


def home_page(request):
    return render(request, 'JKH_site/home_page.html')


def info(request):
    return render(request, 'JKH_site/info.html')


def trades(request, slug=None):
    category = None
    products = Product.objects.all()
    categories = Category.objects.all()
    if slug:
        category = get_object_or_404(Category, slug=slug)
        products = products.filter(product_category=category)
    context = {'category': category, 'categories': categories, 'products': products}
    return render(request, 'JKH_site/trades.html', context)


@login_required
def user_logout(request):
    logout(request)
    return redirect('JKH_site:home_page')


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('JKH_site:home_page')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'JKH_site/profile.html', {'user_form': user_form, 'profile_form': profile_form})


@login_required
def my_products(request):
    products = Product.objects.filter(user=request.user)
    context = {'products': products}
    return render(request, 'JKH_site/my_products.html', context)


@login_required
def product_adding(request):
    user = request.user
    form = ProductAddingForm(request.POST, request.FILES)
    if form.is_valid():
        product = form.save(commit=False)
        product.user = user
        product.save()
        return redirect('JKH_site:my_products')
    else:
        form = ProductAddingForm()
    return render(request, 'JKH_site/product_adding.html', {'form': form})


@login_required
def product_delete(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect('JKH_site:my_products')
