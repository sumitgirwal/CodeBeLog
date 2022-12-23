from django.shortcuts import render, redirect

from .models import User
from .forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404

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
def userLogout(request):
    logout(request)
    return redirect('/')



# User account view
def viewUser(request, pk):
     
    user = get_object_or_404(User, pk=1)
    context = {
        'user': user
    }
    return render(request, 'user-profile.html', context)