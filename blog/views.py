from django.views import generic
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Vocab
from datetime import datetime


posts_per_page = 5

def index(request):
    CY = datetime.today().year
    all_notes = Post.objects.all()
    r_notes = all_notes.filter(category=0).count()
    c_notes =  all_notes.count()-r_notes
    return render(request, 'base.html', {'CY': CY, 'r_notes': r_notes,'c_notes':c_notes})

def about(request):
    return render(request, 'base.html', {})

def vocab(request):
    # words = Vocab.objects.all().order_by('?')
    words = Vocab.objects.values('russian','english').order_by('?')
    return render(request, 'vocab.html', {'words':words})

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
