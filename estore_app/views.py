from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth import authenticate
# Create your views here.

def register(request): # function to register a user
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2: #checking if the first and the second password match
            if User.objects.filter(username = username).exists():
                messages.error(request, 'the username is taken. try another username')
            elif User.objects.filter(email = email).exists():
                messages.error(request, 'the email is in user. find another one')
            else:
                user = User.objects.create_user(first_name = firstname, last_name = lastname, username = username, email = email, password = password)
                return redirect('login')
        else:
            messages.error(request, 'the passwords dont match')
            return redirect('register')

    return render(request, 'register.html')

def login(request): #function to login a user
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = auth.authenticate(username = username , password = password) # checking if the user credentials match the ones in the database
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'the user does not exist')
            return redirect('login')
        
    return render(request, 'login.html')

def logout(request): #function to logout a user
    auth.logout(request)
    return render(request, 'logout.html')


