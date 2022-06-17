# Generated by Django 4.0.5 on 2022-06-17 14:35

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NeighbourHood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('health_email', models.EmailField(default='', max_length=100)),
                ('health_center', models.CharField(default='', max_length=100)),
                ('health_contact', models.IntegerField(blank=True, default=0, null=True)),
                ('police_email', models.EmailField(default='', max_length=100)),
                ('police_center', models.CharField(default='', max_length=100)),
                ('police_contact', models.IntegerField(blank=True, default=0, null=True)),
                ('location', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('bio', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=60)),
                ('phone_no', models.IntegerField(blank=True)),
                ('post_date', models.DateTimeField(auto_now=True)),
                ('neighbourhood', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='neighbour', to='hood.neighbourhood')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
