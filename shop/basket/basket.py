from decimal import Decimal
from django.shortcuts import get_object_or_404

from ..models import Products

class Basket():
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket

    def __len__(self):
        return sum(item['qty'] for item in self.basket.values())

    def __iter__(self):
        basket = self.basket
        for item in basket.keys():
            product = get_object_or_404(Products, id=int(item))
            basket[item]['product'] = product
            basket[item]['total'] = int(basket[item]['qty']) * product.price
            yield basket[item]

    def subtotal(self):
        subtotal = Decimal(0)
        for product in self.basket.values():
            subtotal += int(product['qty']) * Decimal(product['price'])
        return subtotal
        # return sum(Decimal(item['price']) * item['qty'] for item in self.basket.values())

    def add(self, product, product_qty):
        product_id = str(product.id)
        if product_id in self.basket:
            self.basket[product_id]['qty'] = product_qty
        else:
            self.basket[product_id] = {'price': str(product.price), 'qty': product_qty}

        self.save()

    update = add

    def delete(self, product_id):
        del self.basket[product_id]
        self.save()

    def save(self):
        self.session.modified = True
