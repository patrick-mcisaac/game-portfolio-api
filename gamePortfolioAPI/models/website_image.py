from django.db import models


class WebsiteImage(models.Model):
    image = models.ImageField(upload_to="website_image")
    website = models.ForeignKey(
        "Website", on_delete=models.CASCADE, related_name="images"
    )
