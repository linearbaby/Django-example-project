from django.contrib import admin

# Register your models here.


from .models import Products, Category

admin.site.register(Products)
admin.site.register(Category)
