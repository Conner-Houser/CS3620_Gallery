from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to="images/")
    session_key = models.CharField(max_length=40, blank=True, null=True)
    tags = models.CharField(max_length=100, blank=True, help_text="Add tags separated by commas")