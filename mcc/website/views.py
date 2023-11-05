from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Position

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


@login_required
def positions(request):
    positions = Position.objects.all()
    return render(request, 'positions.html', {"positions": positions})

@login_required
def add_position(request):
    if request.method == 'POST':
        name = request.POST['positionName']
        status = request.POST['positionStatus']
        description = request.POST['positionDescription']

        position = Position(name=name, description=description, status=status)
        position.save()
        messages.success(request, "Position Added!")
    return redirect('positions')

@login_required
def delete_position(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        try:
            instance = Position.objects.get(pk=id)
            instance.delete()
            messages.success(request, "Position Deleted!")
        except Position.DoesNotExist:
            messages.success(request, "Error: Position does not exist. Could not be deleted")
    return redirect('positions')