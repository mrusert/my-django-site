from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post # the . means current directory or current application

# Create your views here.

def post_list(request):
    # Query for posts with published date and order by the same
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # Return posts query in render object
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    # Throw 404 if post id doesn't exist
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})