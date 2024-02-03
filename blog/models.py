from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
# From I think before I blog walkthrough and Youtube Video for image
class Post(models.Model): 
    title = models.CharField(max_length=200, unique = True)
    slug = models.SlugField(max_length=200, unique = True)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="art_posts")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)

# from I think before I blog walkthrough
class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)