from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from blog.models import Article


def hello(request):
    # return HttpResponse('hello blog')
    return render(request, 'index.html')


def blog_list(request):
    articles = Article.objects.all()
    return render(request, 'blog_list.html', {'articles': articles,
                                              })