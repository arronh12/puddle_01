from django.db import models
from django.contrib.auth.models import User


class Dept(models.Model):

    def __str__(self):
        return 'Dept Name: ' + self.dept_name

    dept_choices = (
        ('Vis', 'Vis'),
        ('Sound', 'Sound'),
        ('Lighting', 'Lighting'),
        ('Transmission', 'Transmission')
    )

    dept_name = models.CharField(max_length=20, choices=dept_choices)
    dept_head = models.CharField(max_length=50, default='')


class AccountProfile(models.Model):

    def __str__(self):
        return 'User Name: ' + self.user.username

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_no = models.CharField(max_length=20, default='')
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE, default='')
    first_name = models.CharField(max_length=100, default='')
    last_name = models.CharField(max_length=100, default='')
    account_type = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=100, default='')
    email = models.CharField(max_length=250, default='')
    current_job_id = models.CharField(max_length=20, default='')

