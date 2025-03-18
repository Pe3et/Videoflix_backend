from django.contrib import admin

from video_app.models import Video
from video_app.tasks import convert_video

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):

    """
    When uploading a new video to the admin panel, the task for celery to convert the video file
    will be called.
    """
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        convert_video.delay(obj.id)