from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
# From I think before I blog walkthrough and Youtube Video for image
class Uploads(models.Model): 
    title = models.CharField(max_length=200, unique=True)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    artist = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="art_uploads")
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    class Meta:
        ordering = ["-created_on"]
    def __str__(self):
        return f"This artwork is titled {self.title} | uploaded by {self.artist}"

# from I think before I blog walkthrough
class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    num_stars = models.IntegerField()
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Comment {self.body} by {self.artist}"

