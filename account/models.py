from django.db import models
from django.contrib.auth.models import User


class Dept(models.Model):

    def __str__(self):
        return self.dept_name

    dept_choices = (
        ('Vis', 'Vis'),
        ('Sound', 'Sound'),
        ('Lighting', 'Lighting'),
        ('Transmission', 'Transmission'),
        ('Admin', 'Administration'),
        ('edt', 'Editing')
    )

    dept_name = models.CharField(max_length=20, choices=dept_choices)
    dept_head = models.ForeignKey(User, on_delete=models.CASCADE, default='')


class AccountProfile(models.Model):

    def __str__(self):
        return 'User Name: ' + self.user.username

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_no = models.CharField(max_length=20, default='')
    phone_num = models.CharField(max_length=20, default='')
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE)

