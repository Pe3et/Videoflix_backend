from rest_framework import serializers

from video_app.tasks import convert_video
from .models import Video


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

    """
    Creates converted video files with different resolution.
    """
    def create(self, validated_data):
        print('DOES THIS EVEN FIRE?')
        video = super().create(validated_data)
        convert_video(video.id)
        return video