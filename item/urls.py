from item.views import UserHomeView
from item.views import EquipmentAddItemView
from django.urls import path
from django.contrib.auth.views import LoginView

from . import views


app_name = "item"

urlpatterns = [
    path('', UserHomeView.as_view(), name='UserHome'),
    path('Equipment/', views.EquipmentView, name='Equipment'),
    path('add_item/', EquipmentAddItemView.as_view(), name='add_item')
]

