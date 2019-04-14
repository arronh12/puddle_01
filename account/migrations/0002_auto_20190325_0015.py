# Generated by Django 2.1.5 on 2019-03-25 00:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_name', models.CharField(choices=[('Vis', 'Vis'), ('Sound', 'Sound'), ('Lighting', 'Lighting'), ('Transmission', 'Transmission')], max_length=20)),
                ('dept_head', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='accountprofile',
            name='dept',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='account.Dept'),
        ),
    ]