# Generated by Django 5.1.2 on 2024-11-18 09:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0005_address_default'),
        ('wasteapp', '0004_alter_wasterequest_collection_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wasterequest',
            name='collection_location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profileapp.address'),
        ),
    ]
