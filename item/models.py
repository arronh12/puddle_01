from django.db import models
from account.models import AccountProfile
from account.models import User, Dept


class Items(models.Model):

    def __str__(self):
        return 'Item Name: ' + self.item_name

    item_barcode = models.CharField(max_length=20, default='')
    item_name = models.CharField(max_length=200, default='')
    item_type = models.CharField(max_length=200, default='')
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE, default='')
    current_employee = models.CharField(max_length=20, default='')
    item_amount = models.IntegerField()
    item_description = models.TextField(max_length=500, default='')
    item_notes = models.TextField(max_length=500, default='')




