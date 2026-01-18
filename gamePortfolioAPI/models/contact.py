from django.db import models


class Contact(models.Model):
    """
    Contact class for a developer
    """

    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    developer = models.ForeignKey(
        "Developer", on_delete=models.CASCADE, related_name="contact"
    )

    def __str__(self):
        return f"{self.name}"
