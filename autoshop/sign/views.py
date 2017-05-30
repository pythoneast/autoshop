from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
# from django.views.decorators.http import require_POST
from autoshop.sign.decorators import is_anonymous
from django.contrib.auth import authenticate, login

from autoshop.sign.forms import SignInForm, SignUpForm


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
    return render(request, 'sign/signin.html', locals())


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
    return render(request, 'sign/signup.html', locals())


@login_required
# @require_POST
def signout(request):
    logout(request)
    return redirect('index-main')
