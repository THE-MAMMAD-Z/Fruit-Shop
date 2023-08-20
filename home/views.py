from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import ContactForm


def home(request):
    return render(request,'home/index.html')

def contact(request):
    if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request,'home/success.html')  # Replace 'contact_success' with the URL name for the success page
    else:
        form = ContactForm()

    return render(request, 'home/contact.html', {'form': form})



def about(request):
    return render(request,'home/about.html')