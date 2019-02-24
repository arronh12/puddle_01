from django.db import models
from django.contrib.auth.models import User


class AccountProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_no = models.CharField(max_length=20, default='')
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    account_type = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=100, default='')
    email = models.CharField(max_length=250, default='')
    current_job_id = models.CharField(max_length=20, default='')
