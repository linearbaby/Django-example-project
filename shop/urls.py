from django.urls import path, include
from . import views as shop_views
from .basket import views as basket_views

app_name = 'shop'

basket_urlpatterns = [
    path('', basket_views.summary, name='basket_summary'),
    path('add/', basket_views.add, name='basket_add'),
    path('delete/', basket_views.delete, name='basket_delete'),
    path('update/', basket_views.update, name='basket_update'),
]

urlpatterns = [
    path('', shop_views.main, name='main'),
    path('<int:page>', shop_views.main, name='main'),
    path('category/<slug:slug>', shop_views.category_list, name='category'),
    path('product/<slug:slug>', shop_views.product_detail, name='product_detail'),
    path('basket/', include(basket_urlpatterns)),
]
