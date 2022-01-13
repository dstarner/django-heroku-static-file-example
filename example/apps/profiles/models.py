import pathlib

from django.contrib.auth import get_user_model
from django.db import models


def _profile_avatar_upload_path(instance, filename):
    """Provides a clean upload path for user avatar images
    """
    file_extension = pathlib.Path(filename).suffix
    return f'avatars/profiles/{instance.user.username}{file_extension}'


class UserProfile(models.Model):

    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)

    avatar = models.ImageField(upload_to=_profile_avatar_upload_path)

    about_me = models.TextField()

    def __str__(self) -> str:
        return f'Profile for {self.user.username}'
