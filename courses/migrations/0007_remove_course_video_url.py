# Generated by Django 5.1.5 on 2025-02-26 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_alter_lesson_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='video_url',
        ),
    ]
