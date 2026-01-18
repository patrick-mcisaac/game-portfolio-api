from django.db import models


class Game(models.Model):
    """
    Model for game
    """

    title = models.CharField(max_length=255)
    description = models.TextField()
    link = models.CharField(max_length=255)
    learned = models.TextField()
    developer = models.ForeignKey(
        "Developer", on_delete=models.CASCADE, related_name="games"
    )
