from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from .forms import MyUserCreationForm, LoginForm
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

# Create your views here.
@login_required
def index(request):
    return render(request, 'basic_app/main.html')


def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:      
        return successfulLogin(request)  
    
    if request.method == 'POST':
       form = LoginForm(request.POST)
       if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            try:
                user = User.objects.get(username)
            except:
                messages.error(request, 'User does not exist')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return successfulLogin(request)
            else:
                messages.error(request, 'Username OR password does not exit')
    else:
          form = LoginForm()
          
    context = {'page': page, 'form':form}
    return render(request, 'basic_app/login_register.html', context)

def logoutUser(request):
    logout(request)
    return successfulLogin(request)


def successfulLogin(request):
    return render(request, 'basic_app/successful_login.html')

def registerPage(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.password = make_password('password') 
            user.save()
            login(request, user)
            return successfulLogin(request)
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'basic_app/login_register.html', {'form': form})
