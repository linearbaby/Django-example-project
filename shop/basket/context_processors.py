from .basket import Basket


def basket(request):
    basket1 = Basket(request)
    return {'basket': basket1}
