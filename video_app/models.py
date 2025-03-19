from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

class Video(models.Model):
    CATEGORIES = [
        ('cats', 'Cats'),
        ('cities', 'Cities'),
        ('nature', 'Nature')
    ]

    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    original_file = models.FileField(upload_to='videos/')
    processed_120p = models.FileField(null=True, blank=True)
    processed_360p = models.FileField(null=True, blank=True)
    processed_720p = models.FileField(null=True, blank=True)
    processed_1080p = models.FileField(null=True, blank=True)
    thumbnail = models.FileField(upload_to='thumbnails/')
    category = models.CharField(max_length=255, choices=CATEGORIES, default='cats')

    def __str__(self):
        return self.title


@receiver(post_delete, sender=Video)
def delete_video_files(sender, instance, **kwargs):
    """
    Deletes files from the filesystem when the Video instance is deleted.
    """
    if instance.original_file:
        instance.original_file.delete(save=False)
    if instance.processed_120p:
        instance.processed_120p.delete(save=False)
    if instance.processed_360p:
        instance.processed_360p.delete(save=False)
    if instance.processed_720p:
        instance.processed_720p.delete(save=False)
    if instance.processed_1080p:
        instance.processed_1080p.delete(save=False)
    if instance.thumbnail:
        instance.thumbnail.delete(save=False)