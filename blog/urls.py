from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.index, name='about'),
    path('vocab/', views.vocab, name='vocab'),
    path('russian/', views.PostListRussian.as_view(), name='russian'),
    path('coding/', views.PostListCoding.as_view(), name='coding'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
