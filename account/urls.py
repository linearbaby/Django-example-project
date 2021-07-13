from django.urls import path, include
from django.contrib.auth import views
from . import views as loc_views
from . import forms
from django.views.generic import TemplateView


app_name = 'account'

urlpatterns = [
    path('login', views.LoginView.as_view(template_name='account/login.html',
                                          authentication_form=forms.LoginForm), name='login'),
    path('registration', loc_views.registration, name='registration'),
    path('registration_done/<slug:uidb64>/<slug:token>', loc_views.account_activation, name='activate'),
    path('dashboard', TemplateView.as_view(template_name='account/dashboard.html'), name='dashboard')
]