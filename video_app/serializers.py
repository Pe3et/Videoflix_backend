from rest_framework import serializers

from video_app.tasks import convert_video
from .models import Video


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'