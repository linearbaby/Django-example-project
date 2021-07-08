from django.shortcuts import get_object_or_404, render
from .models import Products, Category


def main(request, page=1):
    products = Products.objects.all()
    return render(request, 'shop/home.html', {'products': products})


def category_list(request, slug, page=1):
    category = get_object_or_404(Category, slug=slug)
    products = Products.objects.filter(category=category)
    return render(request, 'shop/category.html', {'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Products, slug=slug)
    return render(request, 'shop/product_detail.html', {'product': product})
