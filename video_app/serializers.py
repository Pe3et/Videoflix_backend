from rest_framework import serializers

from video_app.tasks import convert_video
from .models import Video


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

    """
    Calls the tasks for creation of converted video files with different resolution.
    """
    def create(self, validated_data):
        video = super().create(validated_data)
        convert_video(video.id)
        return video