from django.db import models
from django.contrib.auth.models import AbstractUser
from logic.viewscript import upload_path

class CustomUser(AbstractUser):
    email = models.EmailField(blank=False,null=False)
    profile_photo = models.ImageField(upload_to=upload_path, null=True, blank = True)
    def __str__(self):
        return self.username