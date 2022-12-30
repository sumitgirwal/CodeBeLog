from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post, Category, Comment
from .forms import PostForm, PostEditForm, CommentForm

from django.views import generic
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from django.urls import reverse

 

 

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

    posts = Post.objects.filter(auther=request.user)
    post_likes = 0
    for i in posts:
       post_likes += i.likes.count() 
    
    post_count = posts.count()
    followers = 0
    following = 0
    context = { 
            'form':PostForm(), 
            'msg':msg,
            'post_count':post_count,
            'post_likes':post_likes,
            'followers': followers,
            'following': following
        }
    return render(request, 'create-post.html', context )


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

    posts = Post.objects.filter(auther=request.user)
    post_likes = 0
    for i in posts:
       post_likes += i.likes.count() 
    
    post_count = posts.count()
    followers = 0
    following = 0
    context = { 
        'form':PostForm(instance=post), 
        'post':post, 
        'msg':msg,
        'post_count':post_count,
        'post_likes':post_likes,
        'followers': followers,
        'following': following
    
    }
    return render(request, 'create-post.html', context )

 
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
    post = None
    try:
        post = Post.objects.get(id=pk, auther=request.user)
    except Exception as e:
        print(e)

    if request.method=='POST':
        post.delete()
        return redirect('my_post')

    
    
    posts = Post.objects.filter(auther=request.user)
    post_likes = 0
    for i in posts:
       post_likes += i.likes.count() 
    
    post_count = posts.count()

    followers = 0
    following = 0
    context = {
        'post': post,
        'post_count': post_count,
        'post_likes':post_likes,
        'followers': followers,
        'following': following
    }
    return render(request, 'delete-post.html', context)




# View a Post
def viewPost(request, slug):
    post = Post.objects.get(slug=slug)
    cats = post.category.all()
    # post = get_object_or_404(BlogPost, id=request.POST.get('blogpost_id'))
    
    # Update the view count
    session_key = 'key_'+str(post.id)
    if not request.session.get(session_key, False):
        Post.objects.filter(id=post.id).update(view=post.view+1)
        request.session[session_key] = True 
    
    msg = ''
    if request.method=='POST':
        if request.user.is_authenticated:
            if request.POST.get('body', False):
                body = request.POST.get('body')
                comment = Comment(auther=request.user, post=post, body=body)
                comment.save()
                msg = "Comment added successfully!!! Wait for approved by admin"
            elif  request.POST.get('like', False):
                if post.likes.filter(id=request.user.id).exists():
                    post.likes.remove(request.user)
                else:
                    post.likes.add(request.user)

                Post.objects.filter(id=post.id).update(like=request.user)
                msg = "Added like to post!!!" 

        else:
            msg = "Please login first"

    comments = Comment.objects.filter(post=post, status=True).order_by('-created_at')
    comments_count = comments.count()
     
    # Like a post
    likes_connected = post
    liked = False
    if likes_connected.likes.filter(id=request.user.id).exists():
        liked = True
    number_of_likes = likes_connected.number_of_likes()
    post_is_liked = liked
    context = {
        'number_of_likes':number_of_likes,
        'post_is_liked':post_is_liked,
        'object':likes_connected,
        'post':post, 'cats':cats, 'msg':msg, 'comments':comments, 'comments_count':comments_count
    }
    return render(request, 'view-post.html', context)



def BlogPostLike(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('blogpost_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    slug = post.slug
    return HttpResponseRedirect(reverse('view_post', args=[str(slug)]))




@login_required(login_url='/account/login/')
def myPost(request):
    posts = Post.objects.filter(auther=request.user)
    post_likes = 0
    for i in posts:
       post_likes += i.likes.count() 
    followers = 0
    following = 0
    context = {
        'posts':posts,
        'post_count':posts.count(),
        'post_likes':post_likes,
        'followers': followers,
        'following': following
    }
    return render(request, 'my-post.html', context)


# Like a post 
@login_required(login_url='/account/login/')
def likePost(request):
    msg = ''
    if request.method=='POST':
        like = request.POST['post_id']
        msg = str(like)+'Getting post id like value'
         
        return
    else:
        return





# def BlogDetails(request, pk):
#     likes_connected = Post.objects.get(id=pk)
#     liked = False
#     if likes_connected.likes.filter(id=request.user.id).exists():
#         liked = True
#     number_of_likes = likes_connected.number_of_likes()
#     post_is_liked = liked
#     context = {
#         'number_of_likes':number_of_likes,
#         'post_is_liked':post_is_liked,
#         'object':likes_connected
#     }
#     return render(request, 'temp.html', context)
