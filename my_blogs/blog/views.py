from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request): 
    #return HttpResponse("this is home page")
    return render(request, 'index.html')  # but before using the template, we have to specify the template path into the setting.py


def about(request): 
    # return HttpResponse("this is About page")
    return render(request, 'about/index.html')  # accessing the template in nested


def contact(request): 
    return HttpResponse("this is Contact page")