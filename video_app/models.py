from django.db import models

class Video(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    original_file = models.FileField(upload_to='videos/')
    processed_120p = models.FileField(null=True, blank=True)
    processed_360p = models.FileField(null=True, blank=True)
    processed_720p = models.FileField(null=True, blank=True)
    processed_1080p = models.FileField(null=True, blank=True)
    thumbnail = models.FileField(upload_to='thumbnails/', blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title
    
    def delete(self, *args, **kwargs):
        self.original_file.delete()
        self.processed_120p.delete()
        self.processed_360p.delete()
        self.processed_720p.delete()
        self.processed_1080p.delete()
        super().delete(*args, **kwargs)