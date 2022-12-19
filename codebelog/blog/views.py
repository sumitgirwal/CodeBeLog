from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Post
from .forms import PostForm

# Home 
def index(request):
    posts = Post.objects.all()

    context = {
        'posts':posts
    }
    return render(request, 'index.html', context)


# Post Creation
def createPost(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = PostForm()
    context = {
        'form':form
    }
    return render(request, 'create-post.html', context)


# Delete a Post
def deletePost(request, pk):
    try:
        post = Post.objects.get(id=pk)
    except:
        pass

    if request.method=='POST':
        post.delete()
        return redirect('/')
        
    context = {
        'post': post
    }
    return render(request, 'delete-post.html', context)


# Update a Post
def updatePost(request, pk):
    try:
        post = Post.objects.get(id=pk)
    except:
        pass

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post )
        if form.is_valid():
            form.save()
            return redirect('/')

    form = PostForm(instance=post)
    context = {
        'form':form,
        'post':post
    }
    return render(request, 'update-post.html', context)


# View a Post
def viewPost(request, pk):
    try:
        post = Post.objects.get(id=pk)
      
        
    except:
        pass
    context = {
         
        'post':post
    }

    return render(request, 'view-post.html', context)