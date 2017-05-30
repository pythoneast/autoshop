from autoshop.users.forms import SignInForm, SignUpForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from autoshop.users.decorators import is_anonymous


@is_anonymous
def signin(request):
    form = SignInForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user is None:
                messages.error(request, 'Email or password is not correct')
            else:
                if user.is_active:
                    login(request, user)
                    return redirect('index-main')
                else:
                    messages.error(request, 'Your account is disabled')
        else:
            messages.error(request, 'Error', extra_tags='alert')
    return render(request, 'users/signin.html', locals())


@is_anonymous
def signup(request):
    form = SignUpForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user is None:
                messages.error(request, 'Email or password is not correct')
            else:
                if user.is_active:
                    login(request, user)
                    return redirect('index-main')
                else:
                    messages.error(request, 'Your account is disabled')
        else:
            messages.error(request, 'Error', extra_tags='alert')
    return render(request, 'users/signup.html', locals())


@login_required
# @require_POST
def signout(request):
    logout(request)
    return redirect('index-main')
