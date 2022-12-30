from django.shortcuts import render, redirect, get_object_or_404

from account.models import User
from blog.models import Post, Category
from .forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# User signup
def userSignup(request):
    msg = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'login.html', {'msg':'Successfully Signup 😊', 'status':'success'})
        else:
            msg = form.errors
    form = UserCreationForm()
    context = {
        'form':form,
        'msg':msg
    }
    return render(request, 'signup.html', context)

# User Login
def userLogin(request):
    msg = ''
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            msg = "Email or Password is Wrong!!!"
    context = {
        'msg': msg
    }
    return render(request, 'login.html', context)


# User Login
@login_required
def userLogout(request):
    logout(request)
    return redirect('/')



# User account view
@login_required
def viewUser(request, pk):     
    user = get_object_or_404(User, pk=1)
    context = {
        'user': user
    }
    return render(request, 'user-profile.html', context)



@login_required(login_url='/account/login/')
def dashboard(request):
    post_count = Post.objects.filter(auther=request.user).count() 
    posts = Post.objects.filter(auther=request.user)
    post_likes = 0
    for post in posts:
       post_likes += post.likes.count() 

    followers = 0
    following = 0 
    context = {
        'user':request.user,
        'post_count':post_count,
        'post_likes':post_likes,
        'followers': followers,
        'following': following
    }
    return render(request, 'dashboard.html', context)















