# Generated by Django 5.0.4 on 2025-04-06 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='account_type',
            field=models.CharField(choices=[('full', 'Full Package'), ('free', 'Free Package')], default='free', max_length=30),
        ),
    ]
