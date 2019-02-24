from item.views import UserHomeView
from item.views import EquipmentHomeView
from django.urls import path
from django.contrib.auth.views import LoginView


app_name = "item"

urlpatterns = [
    path('', UserHomeView.as_view(), name='UserHome'),
    path('Equipment/', EquipmentHomeView.as_view(), name='Equipment'),
]

