from django.shortcuts import render, redirect

from .models import Post


def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', context={'posts': posts})


def update_like(request, pk):
    post = Post.objects.get(pk=pk)
    post.likes = post.likes + 1
    post.save()
    return redirect('/')
