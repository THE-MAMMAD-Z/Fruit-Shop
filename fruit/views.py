from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from django.contrib.auth import authenticate
from .models import *
from accounts import views
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from fruit.forms import SearchForm


@login_required
def fruits(request) : 
        search=SearchForm(request.GET)
        if search.is_valid():
            searchText=search.cleaned_data["SearchText"]
            mive=Fruit.objects.filter(name__contains=searchText)
        else :
            mive=Fruit.objects.all()

        context = {
            "fruits" : mive,
            "search" : search
        }

        return render(request,'fruit/fruit.html',context)
    # else:
    #     return HttpResponseRedirect(reverse("account:loginn"))
    
def testmonial(request) : 
    return render(request,'fruit/testimonial.html')