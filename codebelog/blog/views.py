from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Post, Category
from .forms import PostForm, PostEditForm

from django.views import generic
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


# Convert text to slug 
def textToSlug(text):
    newTxt = ''
    for i in text:
        if i==' ':
            newTxt += '-'
        elif i.isalnum():
            newTxt += i
    newTxt = newTxt.strip('-')
    return newTxt

# Create a Post
@login_required(login_url='/account/login/')
def createPost(request):
    msg = ''
    if request.method=='POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.auther = request.user
            post.slug = textToSlug(post.title)
            post.save()
            form.save_m2m()
            return redirect('my_post')
        else:
            msg = form.errors 
    return render(request, 'create-post.html', { 'form':PostForm(), 'msg':msg } )


# Update a Post
@login_required(login_url='/account/login/')
def updatePost(request, pk):
    try:
        post = Post.objects.get(id=pk)
    except:
        pass

    msg = ''
    if request.method=='POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.slug = textToSlug(post.title)
            post.save()
            form.save_m2m()
            return redirect('my_post')
        else:
            msg = form.errors 
    return render(request, 'create-post.html', { 'form':PostForm(instance=post), 'post':post, 'msg':msg } )

# Post Creation
# @login_required(login_url='/account/login/')
# def createPost(request):
#     msg = ''
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         if form.is_valid():
#             instance = form.save(commit=False)
#             instance.user = request.user
#             instance.save()
#             return redirect('my_post')
#         else:
#             msg = form.errors
#     form = PostForm()
#     context = {
#         'form':form,
#         'msg':msg
#     }
#     return render(request, 'create-post.html', context)

# # Update a Post
# @login_required(login_url='/account/login/')
# def updatePost(request, pk):
#     post = None
#     msg = ''
#     try:
#         post = Post.objects.get(id=pk, user=request.user)
#     except:
#         pass
    
#     if request.method == 'POST':
#         form = PostForm(request.POST, instance=post)
#         # form = PostForm(request.POST, instance=post , user=request.user)
#         if form.is_valid():
#             form.save()
#             return redirect('my_post')
#         else:
#             msg = form.errors

#     # form = PostForm(instance=post, user=request.user)
#     form = PostForm(instance=post)
#     context = {
#         'form':form,
#         'post':post,
#         'form_action':'edit',
#         'msg':msg
#     }
#     return render(request, 'create-post.html', context)





 

# Home 
def index(request):
    search = request.GET.get('search','')
    posts = None
    if search != '':
        posts = Post.objects.filter(
            Q(status=0) &
            (
                Q(title__icontains=search) |
                Q(subtitle__icontains=search) |
                Q(category__name__icontains=search) 
            )
            ).order_by('-created_at')
    else:
        posts = Post.objects.filter(status=0).order_by('-created_at')

    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 5)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts':posts,
        'cats':Category.objects.all()
    }
    return render(request, 'index.html', context)


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




# View a Post
def viewPost(request, slug):
    post = Post.objects.get(slug=slug)
    # Update the view count
    session_key = f'key_{post.id}'
    if not request.session.get(session_key, False):
        Post.objects.filter(id=post.id).update(view=post.view+1)
        request.session[session_key] = True    
    return render(request, 'view-post.html', {'post':post})


@login_required(login_url='/account/login/')
def myPost(request):
    posts = Post.objects.filter(auther=request.user)
    context = {
        'posts':posts,
        'post_count':posts.count()
    }
    return render(request, 'my-post.html', context)


