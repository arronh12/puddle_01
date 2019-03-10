from django.views.generic import TemplateView
from django.shortcuts import render
from item.models import Items,User
from item.forms import AddForm


class UserHomeView(TemplateView):
    template_name = 'item/item_home.html'


def EquipmentView(request):
    all_items = Items.objects.all()
    context = {
        'all_items': all_items
    }
    return render(request, 'item/equipment.html', context)

class EquipmentAddItemView(TemplateView):
    template_name = 'item/add_item.html'

    def get(self, request):
        form = AddForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()

        return render(request, self.template_name, context={'form': form})





