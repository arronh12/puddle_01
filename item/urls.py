from item.views import UserHomeView
from item.views import EquipmentView
from item.views import EquipmentAddItemView
from django.urls import path

from . import views

app_name = "item"

urlpatterns = [
    path('', UserHomeView.as_view(), name='UserHome'),
    path('Equipment/', EquipmentView.as_view(), name='Equipment'),
    path('add_item/', EquipmentAddItemView.as_view(), name='add_item'),
    path('selected_item/<int:choice>', views.selected_item, name='selected_item'),
]

