from rest_framework.viewsets import ReadOnlyModelViewSet

from video_app.models import Video
from video_app.serializers import VideoSerializer

class VideoViewSet(ReadOnlyModelViewSet):
    queryset = Video.objects.all().order_by('id')
    serializer_class = VideoSerializer
