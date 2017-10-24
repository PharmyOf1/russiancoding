# -*- coding: utf-8 -*-
from django.shortcuts import render
from blog.views import Blog, Category

def home(request):
    data = {'posts': Blog.objects.all()[:5]}
    return render(request, "index.html", data)
