from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request,'home/index.html')

def contact(request):
    return render(request,'home/contact.html')

def about(request):
    return render(request, 'home/about.html')