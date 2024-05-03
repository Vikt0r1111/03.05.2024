from django.shortcuts import render, redirect
from .models import Author, Post, Comment
from .models import Post, Comment
from .forms import CommentForm
from django.contrib import messages

def view(request):
   
    author = Author.objects.first()

    
    comment_count = author.posts.count()

    
    long_comment_count = Comment.objects.filter(post__author=author, text__length__gte=5).count()

    context = {
        'author': author,
        'comment_count': comment_count,
        'long_comment_count': long_comment_count,
    }
    return render(request, 'app_name/stats.html', context)

def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    comments = Comment.objects.filter(post=post)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            author = form.cleaned_data['author']
            content = form.cleaned_data['content']
            Comment.objects.create(post=post, author=author, content=content)
            messages.success(request, 'Your comment was added successfully.')
            return redirect('post_detail', post_id=post_id)
    else:
        form = CommentForm()
    return render(request, 'myapp/post_detail.html', {'post': post, 'comments': comments, 'form': form})