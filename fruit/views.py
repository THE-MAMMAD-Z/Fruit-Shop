from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def fruits(request) : 
    return render(request,'fruit/fruit.html')

def testmonial(request) : 
    return render(request,'fruit/testmonial.html')