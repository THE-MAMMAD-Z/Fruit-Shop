from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.contrib.auth import authenticate, login ,logout
from django.urls import reverse
import fruit
from django.conf import settings
# Create your views here.

def loginn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if request.GET.get('next'):
                return HttpResponseRedirect(request.GET.get("next"))
            return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
        else:
            context = {
                "username": username,
                "errorMessage": "username or password not correct"
            }
            return render(request, 'accounts/login.html', context)
    else:
        return render(request, "accounts/login.html")
    

def logoutt(request):
    logout(request)
    return HttpResponseRedirect(reverse("home:home"))


def profile(request):
    profile=request.user.profile

    context = {
        "profile" : profile,
    }
    return render(request,'accounts/profile.html',context)