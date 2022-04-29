from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def main(request,*args, **kwargs):
    return render(request,'index.html')

def youTube(request,*args, **kwargs):
    return render(request,'static/pages/youtube.html')

def spotify(request,*args, **kwargs):
    return render(request,'static/pages/spotify.html')

def login_user(request,*args, **kwargs):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect("home")
        
        else:
            # Return an 'invalid login' error message.
            messages.success(request,"Invalid: Make sure you typed your Username or Password correctly.")
            return redirect("log-in")
    else:
        return render(request,'static/pages/login.html',{})

def logout_user(request,*args, **kwargs):
    logout(request)
    return redirect("log-in")

def register_user(request,*args, **kwargs):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('log-in')
    else:
        form = UserCreationForm()

    return render(request,'static/pages/signUp.html',{
        'form':form,
    })
