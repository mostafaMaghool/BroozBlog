from django.shortcuts import render
from django.shortcuts import HttpResponse

def about(request):
    #return HttpResponse('hi, How are you')
    return render(request,'about.html')

def home(request):
    #return HttpResponse('home  home   home')
    return render(request,'home.html')
