from blog.models import Blog, Category
from django.shortcuts import render, get_object_or_404

def view_post(request, post_name):
    data = {'post': get_object_or_404(Blog, slug=post_name)}
    print (data['post'])
    return render(request, 'view_post.html', data)

def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render('view_category.html', {
        'category': category,
        'posts': Blog.objects.filter(category=category)[:5]
    })
