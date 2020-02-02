from django.views import generic
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from datetime import datetime

posts_per_page = 5

def index(request):
    CY = datetime.today().year
    return render(request, 'base.html', {'CY': CY})

def about(request):
    return render(request, 'base.html', {})

class PostListRussian(generic.ListView):
    queryset = Post.objects.filter(status=1,category=0).order_by('-created_on')
    template_name = 'posts.html'
    paginate_by = posts_per_page

class PostListCoding(generic.ListView):
    queryset = Post.objects.filter(status=1,category=1).order_by('-created_on')
    template_name = 'posts.html'
    paginate_by = posts_per_page

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
