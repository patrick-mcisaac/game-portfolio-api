from django.db import models


class Website(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    learned = models.TextField(null=True, blank=True)
    developer = models.ForeignKey(
        "Developer", on_delete=models.CASCADE, related_name="websites"
    )

    def __str__(self):
        return f"{self.title}"
