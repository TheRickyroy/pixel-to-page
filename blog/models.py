from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models import Q

STATUS = (
    (0, "Draft"), 
    (1, "Published")
)

def get_default_category():
    category, _ = Category.objects.get_or_create(category="Bullet Journal")
    return category.id

class Category(models.Model):
    """
    Stores the category related to :model: 'blog.Post'
    """
    category = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    default_image = CloudinaryField('image', default='placeholder')
    default_image_alt = models.TextField()
    
    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.category

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.category)
        super().save(*args, **kwargs)

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
    featured_image = CloudinaryField('image', blank=True, null=True)
    featured_image_alt = models.TextField(blank=True)
    category = models.ForeignKey(Category, 
        on_delete=models.PROTECT, related_name="blog_posts", default=get_default_category)
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

    def save(self, *args, **kwargs):
        if not self.featured_image:
            self.featured_image = self.category.default_image
        if not self.slug:
            self.slug = f"{self.category.slug}/{slugify(self.title)}"
        super().save(*args, **kwargs)

    def get_next_post(self):
        return Post.objects.filter(
            Q(created_on__gt=self.created_on) | 
            (Q(created_on=self.created_on) & Q(id__gt=self.id)),
            status=1
        ).order_by('created_on', 'id').first()

    def get_previous_post(self):
        return Post.objects.filter(
            Q(created_on__lt=self.created_on) | 
            (Q(created_on=self.created_on) & Q(id__lt=self.id)),
            status=1
        ).order_by('-created_on', '-id').first()


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