from django.db import models
from account.models import AccountProfile
from item.models import Items


class Job(models.Model):

    def __str__(self):
        return self.job_name

    job_name = models.CharField(max_length=50, default='')
    job_manager = models.ForeignKey(AccountProfile, on_delete=models.CASCADE, default='')
    job_start_date = models.DateField()
    job_end_date = models.DateField()
    get_in_time = models.TimeField()
    items = models.ManyToManyField(Items, through='JobItems', related_name='all_items')


class JobItems(models.Model):
    item_id = models.ForeignKey(Items, related_name='jobItems', on_delete=models.CASCADE, default='')
    job_id = models.ForeignKey(Job, related_name='jobItems', on_delete=models.CASCADE, default='')
