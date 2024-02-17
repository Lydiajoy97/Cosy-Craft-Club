from django.db import models
from django.contrib.auth.models import User

from django.template.defaultfilters import slugify
import os

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
# Youtube Video for image
class Uploads(models.Model): 
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join("media", slugify(self.slug),instance)

    title = models.CharField(max_length=200, unique=True, default=0)
    image = models.ImageField(default="", upload_to=image_upload_to)
    artist = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="art_uploads")
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    class Meta:
        ordering = ["-created_on"]
    def __str__(self):
        return f"This artwork is titled {self.title} | uploaded by {self.artist}"

# Artwork Rating
class Rating(models.Model):

    num_stars = models.IntegerField()
    approved = models.BooleanField(default=False)