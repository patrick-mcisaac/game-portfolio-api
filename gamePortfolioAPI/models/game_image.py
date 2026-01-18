from django.db import models


class GameImage(models.Model):
    """
    Model for game images
    """

    image = models.ImageField(upload_to="game_image")
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name="image")
