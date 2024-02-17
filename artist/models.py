from django.db import models
from django.contrib.auth.models import User

from django.template.defaultfilters import slugify
import os

# Create your models here.
class Bio(models.Model):
    description = models.TextField()

