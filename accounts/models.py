from django.conf import settings
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile"
    )

    phone_number = models.CharField(max_length=11, blank=True)

    def __str__(self):
        return self.user.username
