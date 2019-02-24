from django.db import models


class Items(models.Model):
    item_barcode = models.CharField(max_length=20, default='')
    item_name = models.CharField(max_length=200, default='')
    item_type = models.CharField(max_length=200, default='')
    item_dept = models.CharField(max_length=200, default='')
    current_employee = models.CharField(max_length=20, default='')
    item_amount = models.IntegerField()
    item_description = models.CharField(max_length=500, default='')
    item_notes = models.CharField(max_length=500, default='')


