# Generated by Django 2.1.5 on 2019-03-27 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20190327_1647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accountprofile',
            name='account_type',
        ),
        migrations.RemoveField(
            model_name='accountprofile',
            name='current_job_id',
        ),
        migrations.RemoveField(
            model_name='accountprofile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='accountprofile',
            name='phone_number',
        ),
    ]