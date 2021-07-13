from django.urls import path, include
from django.contrib.auth import views
from .views import registration
from . import forms

app_name = 'account'

urlpatterns = [
    path('login', views.LoginView.as_view(template_name='account/login.html',
                                          authentication_form=forms.LoginForm), name='login'),
    path('registration', registration, name='registration')
]