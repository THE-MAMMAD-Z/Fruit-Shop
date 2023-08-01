from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.contrib.auth import authenticate, login ,logout
from django.urls import reverse
import fruit
from django.conf import settings
from .forms import ProfileRegisterForm
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

def profileregister(request):

    if request.method == "POST":
        profileRegisterForm = ProfileRegisterForm(request.POST, request.FILES)
        if profileRegisterForm.is_valid():
            username = profileRegisterForm.cleaned_data["username"]
            if User.objects.filter(username=username).exists():
                context = {
                    "formData": profileRegisterForm,
                    "errorMessage": "Username already exists. Please choose a different username."
                }
                return render(request, "accounts/profileRegister.html", context)

            user = User.objects.create_user(
                username=username,
                email=profileRegisterForm.cleaned_data['email'],
                password=profileRegisterForm.cleaned_data['password'],
                first_name=profileRegisterForm.cleaned_data['first_name'],
                last_name=profileRegisterForm.cleaned_data['last_name']
            )
            user.save()

            profilemodel = Profile(
                user=user,
                profileimage=profileRegisterForm.cleaned_data['profileimage'],
                Gender=profileRegisterForm.cleaned_data['Gender'],
                phone=profileRegisterForm.cleaned_data['phone'],
                address=profileRegisterForm.cleaned_data['address']
            )
            profilemodel.save()

            return HttpResponseRedirect(reverse("home:home"))
    else:
        profileRegisterForm = ProfileRegisterForm()

    context = {
        "formData": profileRegisterForm
    }

    return render(request, "accounts/profileRegister.html", context)



