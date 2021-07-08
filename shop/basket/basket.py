import copy

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

    def add(self, product, product_qty):
        product_id = str(product.id)
        if product_id in self.basket:
            self.basket[product_id]['qty'] = product_qty
        else:
            self.basket[product_id] = {'price': str(product.price), 'qty': product_qty}

        self.save()

    def save(self):
        self.session.modified = True
