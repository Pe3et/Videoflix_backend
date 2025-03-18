import os
import subprocess
from celery import shared_task
from django.conf import settings
from django.core.files.storage import default_storage

from Videoflix_Backend.settings import VIDEO_RESOLUTIONS
from video_app.models import Video


@shared_task(bind=True, max_retries=3)
def convert_video(self, video_id):
    try:
        video = Video.objects.get(id=video_id)
        input_path = video.original_file.path
        base_name = os.path.splitext(os.path.basename(input_path))[0]
        output_dir = os.path.join(settings.MEDIA_ROOT, 'videos')
        os.makedirs(output_dir, exist_ok=True)

        for resolution, (width, height) in VIDEO_RESOLUTIONS.items():
            output_path = os.path.join(output_dir, f'{base_name}_{resolution}.mp4')
            cmd = [
                'ffmpeg', '-y', '-i', input_path,
                '-vf', f'scale={width}:{height}:force_original_aspect_ratio=decrease,pad={width}:{height}:(ow-iw)/2:(oh-ih)/2:black',
                '-c:v', 'libx264', '-preset', 'fast',
                '-c:a', 'aac', '-b:a', '128k',
                output_path
            ]
            subprocess.run(cmd, check=True)

            with open(output_path, 'rb') as f:
                setattr(video, f'processed_{resolution}', default_storage.save(output_path, f))
                os.remove(output_path)

            video.save()

    except Exception as e:
        self.retry(exc=e, countdown=30)
