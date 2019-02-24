from django.contrib.auth.views import LoginView
from django.urls import path

from . import views

app_name = "account"

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', LoginView.as_view(template_name='account/login.html'), name="login"),
    path('profile/', LoginView.as_view(template_name='account/profile.html'), name='profile'),
]
