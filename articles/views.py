from django.shortcuts import render, HttpResponse
from . import models

def articles_list(request):
    articles = models.Article.objects.all().order_by('date')
    args = {'articles':articles}
    return render(request,'articles/articles_list.html',args)

def articles_details(request, slug):
    return HttpResponse(slug)