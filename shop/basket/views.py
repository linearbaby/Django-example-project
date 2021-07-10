from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import JsonResponse

from .basket import Basket
from ..models import Products


def add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product = get_object_or_404(Products, pk=int(request.POST.get('productid')))
        product_qty = int(request.POST.get('productqty'))
        basket.add(product, product_qty)
        basket_qty = len(basket)
    return JsonResponse({'qty': basket_qty})


def summary(request):
    basket_product_id = Basket(request).basket.keys()
    basket_products = Products.objects.filter(id__in=basket_product_id)
    return render(request, 'shop/summary.html', {'products': basket_products})


def delete(request):
    return HttpResponse('delete')


def update(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Products, id=product_id)
        basket.update(product, product_qty)
        basket_qty = len(basket)
    return JsonResponse({'qty': basket_qty})
