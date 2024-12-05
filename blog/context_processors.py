from .models import Category, Post

def category_context(request):
    categories = Category.objects.all()
    return {'categories': categories}

def global_context(request):
    categories = Category.objects.all()
    featured_posts = Post.objects.filter(featured=True, status=1).order_by('-created_on')[:3]
    return {
        'categories': categories,
        'featured_posts': featured_posts
    }