from django.conf import settings
from django.db import models


class UserProfile(models.Model):
    # user_image = models.ImageField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
