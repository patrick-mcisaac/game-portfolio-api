from django.db import models


class Developer(models.Model):
    """
    Model Class for Developer Info"""

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to="logo", blank=True, null=True)
    about = models.TextField()
