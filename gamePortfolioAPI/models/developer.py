import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class DeveloperManager(UserManager):
    pass


class Developer(AbstractUser):
    """
    Model Class for Developer Info"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="logo", blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    objects = DeveloperManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
