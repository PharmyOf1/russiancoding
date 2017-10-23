from django.conf.urls import url

from .views import view_category, view_post

urlpatterns = [
    url( r'^blog/view/(?P<slug>[^\.]+).html', 'blog.views.view_post', name='view_blog_post'),
    #url(r'^blog/category/(?P<slug>[^\.]+).html','blog.views.view_category', name='view_blog_category'),

]
