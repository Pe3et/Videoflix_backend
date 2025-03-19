from django.urls import include, path
from rest_framework import routers

from video_app.views import VideoViewSet

router = routers.SimpleRouter()
router.register(r'videos', VideoViewSet, basename='videos')

urlpatterns = [
    path('', include(router.urls)),
]