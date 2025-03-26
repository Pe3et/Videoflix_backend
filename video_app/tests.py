import os
from rest_framework.test import APITestCase
from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile

from video_app.models import Video
from video_app.tasks import convert_video

class ConvertTest(APITestCase):

    def setUp(self):
        """
        Adding a test video entry. 
        """
        test_video_path = os.path.join(settings.BASE_DIR, 'media', 'testing_files', 'test_cat.mp4')
        test_thumbnail_path = os.path.join(settings.BASE_DIR, 'media', 'testing_files', 'test_cat_thumbnail.png')
        video_file = SimpleUploadedFile('test.mp4', open(test_video_path, 'rb').read(), content_type='video/mp4')
        thumbnail_file = SimpleUploadedFile('test.png', open(test_thumbnail_path, 'rb').read(), content_type='image/png')
        self.video = Video.objects.create(
            title='Test Video',
            description='Test Description',
            original_file=video_file,
            thumbnail=thumbnail_file,
            category='test category'
        )

    def test_convert(self):
        """
        Testing the functionality of the conversion of a video.
        Deletes the converted files after testing.
        """
        convert_video(self.video.id)
        self.video.refresh_from_db()
        self.assertIsNotNone(self.video.processed_120p.path)
        self.assertIsNotNone(self.video.processed_360p.path)
        self.assertIsNotNone(self.video.processed_720p.path)
        self.assertIsNotNone(self.video.processed_1080p.path)
        self.video.delete()