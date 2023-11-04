from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in!")
            return redirect('home')
        else:
            messages.success(request, "There was an error logging in!")
            return redirect('home')
    else:
        return render(request, 'home.html', {})
    
@login_required
def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out!")
    return redirect('home')