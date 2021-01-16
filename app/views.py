from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from .models import Post, User
from .forms import Login, PostUpload


def index(request, user_id):

    if request.method == 'POST':
        form = PostUpload(request.POST, request.FILES)
        if form.is_valid():
            record = form.save()
            record.user = User.objects.get(id=user_id)
            record.save()
        return redirect(f'/home/{user_id}')
    else:
        posts = Post.objects.all()
        user = User.objects.get(id=user_id)
        create_post = PostUpload()
        return render(request, 'index.html', context={'posts': posts, 'user': user, 'create_post': create_post})


def login(request):
    if request.method == 'POST':
        form = Login(request.POST)
        if User.objects.filter(name=form.data.get('name')).exists():
            user = User.objects.get(name=form.data.get('name'))
            return redirect(f'/home/{user.id}')
        elif form.is_valid():
            form.save()
            user = User.objects.get(name=form.cleaned_data['name'])
            return redirect(f'/home/{user.id}')
        else:
            return HttpResponse(status=500)
    else:
        form = Login()
        return render(request, 'login.html', context={'form': form})


def update_like(request, pk, user_id):
    post = Post.objects.get(pk=pk)
    user = User.objects.get(id=user_id)
    if user in post.likes.all():
        post.likes.remove(user)
    else:
        post.likes.add(user)
    post.save()
    return redirect(f'/home/{user_id}')
