# Generated by Django 5.1 on 2024-11-23 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0006_userprofile_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='is_active',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('user', 'User'), ('driver', 'Driver')], default='user', max_length=10),
        ),
    ]
