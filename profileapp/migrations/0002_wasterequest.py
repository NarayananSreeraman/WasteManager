# Generated by Django 5.1 on 2024-11-11 09:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WasteRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('waste_type', models.CharField(choices=[('Plastic', 'Plastic'), ('Organic', 'Organic'), ('Electronic', 'Electronic'), ('Metal', 'Metal'), ('Paper', 'Paper')], max_length=50)),
                ('quantity', models.PositiveIntegerField(help_text='Enter quantity in kg')),
                ('collection_time', models.DateTimeField()),
                ('collection_loaction', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='waste_requests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
