# Generated by Django 4.0.5 on 2022-06-20 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0004_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
    ]
