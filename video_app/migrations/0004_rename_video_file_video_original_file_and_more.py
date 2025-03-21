# Generated by Django 5.1.6 on 2025-03-18 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_app', '0003_video_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='video_file',
            new_name='original_file',
        ),
        migrations.AddField(
            model_name='video',
            name='processed_1080p',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='video',
            name='processed_120p',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='video',
            name='processed_360p',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='video',
            name='processed_720p',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
