from django.shortcuts import render, get_object_or_404
from .models import Post

def getdate(post):
    return post['date']

def staring_page(request):
    latest_posts = Post.objects.all().order_by('-date')[:3]
    return render(request, 'blogs/index.html', {
        "posts": latest_posts
    })

def all_posts(request):
    latest_posts = Post.objects.all().order_by('-date')
    return render(request, 'blogs/all-posts.html', {
        "posts": latest_posts
    })

def post_details(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, 'blogs/post-detail.html', {
        "post": identified_post,
        "post_tags": identified_post.tags.all()
    })