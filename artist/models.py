from django.db import models
from django.contrib.auth.models import User

from django.template.defaultfilters import slugify
import os

# Create your models here.
class artist(models.Model):
    description = models.TextField()
    artist = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="art_uploads")

