# Generated by Django 5.1.5 on 2025-02-19 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_profile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(default='default.jpg', upload_to='user_images', verbose_name='Фото пользователя'),
        ),
    ]
