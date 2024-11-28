from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = (
    (0, "Draft"), 
    (1, "Published")
)


class Post(models.Model):
    """
    Stores individual blog posts related to :model: 'auth.User'
    """

    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="blog_posts"
    )
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    excerpt = models.TextField(max_length=1024, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"


class Comment(models.Model):
    """
    Stores individual comments related to :model: 'auth-User' and :model: 'blog.Post'
    """

    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, 
        related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="commenter"
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"