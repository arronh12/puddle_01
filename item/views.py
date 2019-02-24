from django.views.generic import TemplateView


class UserHomeView(TemplateView):
    template_name = 'item/item_home.html'


class EquipmentHomeView(TemplateView):
    template_name = 'item/equipment.html'

    

