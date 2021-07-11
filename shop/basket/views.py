from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import JsonResponse

from .basket import Basket
from ..models import Products

from decimal import Decimal, getcontext


def add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product = get_object_or_404(Products, pk=int(request.POST.get('productid')))
        product_qty = int(request.POST.get('productqty'))
        basket.add(product, product_qty)
        basket_qty = len(basket)
    return JsonResponse({'qty': basket_qty, 'subtotal': basket.subtotal()})


def summary(request):
    basket = Basket(request)
    return render(request, 'shop/summary.html', {'subtotal': basket.subtotal(),
                                                 'total': Decimal(basket.subtotal() + Decimal('11.99'))})


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
    return JsonResponse({'qty': basket_qty, 'subtotal': basket.subtotal()})
