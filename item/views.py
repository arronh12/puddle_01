from django.views.generic import TemplateView
from django.shortcuts import render
from item.models import Items, User
from item.forms import AddForm


# Class to view home page of items
class UserHomeView(TemplateView):
    template_name = 'item/item_home.html'


# Class that displays get and post code for the main equipment page
class EquipmentView(TemplateView):
    template_name = 'item/equipment.html'

    def get(self, request):
        all_items = Items.objects.all()
        selected = 0
        context = {
            'all_items': all_items,
            'selected': selected
        }
        return render(request, self.template_name, context)

    def post(self, request):
        all_items = Items.objects.all()
        context = {
            'all_items': all_items
        }
        render(request, self.template_name, context)


# class to display form for user to input an item into the db
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


# def to display details on the users selected item
def selected_item(request, choice):
    item = Items.objects.all()
    item = Items.objects.get(pk=choice)
    context = {
        'choice': choice,
        'item': item,
    }
    return render(request, 'item/selected_item.html', context)


