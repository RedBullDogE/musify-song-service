from django.db import models
from django.conf import settings

class UserProfile(models.Model):
    # user_image = models.ImageField()
    user =  models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )