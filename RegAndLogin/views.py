from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect
from django.template.context_processors import csrf
from django.utils import timezone

from .forms import UserRegistrationForm,UserLoginForm
from django.contrib.auth import authenticate,login,logout,get_user_model


def login_view(request):
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username= form.cleaned_data.get('username')
        password= form.cleaned_data.get('password')
        user = authenticate(username =username,password=password)
        login(request, user)
        return redirect('/index/')


    context = {

        'form': form,
        'title': title
    }

    return render(request, 'registration/login.html', context)

def Register_view(request):
    title = "Register"
    form = UserRegistrationForm(request.POST or None)

    if form.is_valid():
        messo = messages.success(request, 'Registration successfull')

        user =form.save(commit=False)
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')

        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()

        context = {

            'messages': messo
        }

        return redirect('/userauth/login',context)
    context = {

        'form': form,
        'title': title,
    }

    return render(request, 'registration/register.html', context)


