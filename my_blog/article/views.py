# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,Http404
from datetime import datetime
from article.models import Article
# Create your views here.
def home(request):
    post_list = Article.objects.all()
    return render(request,'home.html' , {'post_list':post_list})

def detail(request,id):
    try:
        post = Article.objects.get(id = str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html',{'post':post})

def archives(request):
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist:
        raise Http404
    return render(request,'archives.html',{'post_list':post_list,
                                           'error':False,})

def search_tag(request, tag):
    try:
        post_list = Article.objects.filter(category = tag)
    except Article.DoesNotExist:
        raise Http404
    return render(request,'tag.html',{'post_list':post_list})

def test(request):
    current_time = datetime.now()
    content = {'current_time':current_time,}
    return render(request,'test.html',content)