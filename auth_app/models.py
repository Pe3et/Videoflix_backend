from django.contrib.auth.models import AbstractUser
from django.db import models

class UserProfile(AbstractUser):
    is_email_confirmed = models.BooleanField(default=False)