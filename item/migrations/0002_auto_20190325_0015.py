# Generated by Django 2.1.5 on 2019-03-25 00:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20190325_0015'),
        ('item', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='item_dept',
        ),
        migrations.RemoveField(
            model_name='items',
            name='user',
        ),
        migrations.AddField(
            model_name='items',
            name='dept',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='account.Dept'),
        ),
        migrations.AlterField(
            model_name='items',
            name='item_description',
            field=models.TextField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='items',
            name='item_notes',
            field=models.TextField(default='', max_length=500),
        ),
    ]
