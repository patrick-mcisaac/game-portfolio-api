from django.db import models

class WebsiteLink(models.Model):
    """ 
     Class for website links 
    """
    link = models.CharField(max_length=255)
    website = models.ForeignKey('Website', on_delete=models.CASCADE, related_name='links')

