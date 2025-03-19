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
        if not change:
            convert_video.delay(obj.id)

    from django.contrib import admin

    """
    Defining what fields are readonly for admins and access to original_file & thumbnail is only
    for creation, not for changing.
    """
    def get_readonly_fields(self, request, obj=None):
        readonly_fields = ['created_at', 'processed_120p','processed_360p', 'processed_720p', 'processed_1080p'] 
        if obj:  
            return readonly_fields+['original_file', 'thumbnail']
        return readonly_fields
