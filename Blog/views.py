from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Post
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


# Create your views here.

@login_required
def home(request):

    print(request.user.id)

    posts = Post.objects.all().order_by('-date')

    context = {
        'posts': posts 
        }

    return render(request, 'blog/home.html', context)

@login_required
def createPost(request):

    if request.method == 'POST':

        post = Post(
            title = request.POST.get('title'),
            desc = request.POST.get('desc'),
            user_id = request.user.id
        )

        post.save()    

        return redirect('/home')

    else:
        return render(request, 'blog/createPost.html')

@login_required
def editPost(request, pk):
    if request.method == 'POST':

        title = request.POST.get('title')
        desc = request.POST.get('desc')

        obj = Post.objects.get(id=pk)
        obj.title = title
        obj.desc = desc
        obj.save()

        return redirect('/home')
    
    else:
        post = Post.objects.get(id=pk)

        return render(request, 'blog/editPost.html', {'post': post})

@login_required
def deletePost(request, pk):

    Post.objects.filter(id=pk).delete()

    return redirect('/home')

@login_required
def detailPost(request, pk):

    post = Post.objects.get(id=pk)

    context = {'post': post}

    return render(request, 'blog/detailPost.html', context)

@login_required
def about(request):
    
    return render(request, 'blog/about.html', {'title': 'About'})

