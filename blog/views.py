from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post # the . means current directory or current application
from .forms import PostForm

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

def post_new(request):
    # Check if form submission ("PUT") rather than "GET" request
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            # Submit form and redirect to post detail page
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})