from django import forms

from item.models import Items


class AddForm(forms.ModelForm):

    class Meta:
        model = Items
        fields = ['item_barcode', 'item_name', 'item_type', 'item_dept', 'current_employee', 'item_amount',
                  'item_description', 'item_notes']


