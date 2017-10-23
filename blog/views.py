from blog.models import Blog, Category
from django.shortcuts import render, get_object_or_404

def index(request):
    return render('index.html', {
        'categories': Category.objects.all(),
        'posts': Blog.objects.order_by('-posted').all()[:5]
    })

def view_post(request, slug):
    return render('view_post.html', {
        'post': get_object_or_404(Blog, slug=slug)
    })

def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render('view_category.html', {
        'category': category,
        'posts': Blog.objects.filter(category=category)[:5]
    })
