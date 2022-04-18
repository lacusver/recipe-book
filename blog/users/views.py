from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import login, logout
from .forms import UserSignUpForm, UserSignInForm

def sign_up(request):
    if request.method=='POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully registered!')
            return redirect('sign-in')
        else:
            messages.error(request, 'Registration error!')
    
    else:
        form = UserSignUpForm()
    return render (request, template_name='users/sign_user.html', context={'form':form, 'sign_url':'sign-up'})


def sign_in(request):
    if request.method=='POST':
        form = UserSignInForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'You have successfully log in!')
            return redirect('home')
        else:
            messages.error(request, 'Authentication error!')
    else:
        form = UserSignInForm()
    return render (request, template_name='users/sign_user.html', context={'form':form, 'sign_url':'sign-in'})


def logout_user(request):
    logout(request)
    return redirect('sign-in')