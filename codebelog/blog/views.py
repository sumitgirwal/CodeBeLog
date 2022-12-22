from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Post, Category
from .forms import PostForm

from django.views import generic
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


from django import template
register = template.Library()

@register.inclusion_tag('sidebar.html')
def get_category_list():
    data = {
        'cats': Category.objects.all()
    } 
    return data

# Home 
def index(request):
    search = request.GET.get('search','')
    posts = None
    if search != '':
        posts = Post.objects.filter(
            Q(title__icontains=search) |
            Q(subtitle__icontains=search) 
            )
    else:
        posts = Post.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 5)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts':posts
    }
    return render(request, 'index.html', context)


# Post Creation
@login_required(login_url='/account/login/')
def createPost(request):
    if request.method == 'POST':
        form = PostForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = PostForm(user=request.user)
    context = {
        'form':form
    }
    return render(request, 'create-post.html', context)


# Delete a Post
@login_required(login_url='/account/login/')
def deletePost(request, pk):
    try:
        post = Post.objects.get(id=pk, user=request.user)
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
@login_required(login_url='/account/login/')
def updatePost(request, pk):
    try:
        post = Post.objects.get(id=pk, user=request.user)
    except:
        pass

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post , user=request.user)
        if form.is_valid():
            form.save()
            return redirect('/')

    form = PostForm(instance=post, user=request.user)
    context = {
        'form':form,
        'post':post
    }
    return render(request, 'update-post.html', context)


# View a Post
def viewPost(request, pk):
    try:
        post = Post.objects.get(id=pk)
        post.view += 1
        post.save()
        
    except:
        pass
    context = {
         
        'post':post
    }

    return render(request, 'view-post.html', context)

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'view-post.html'