from django.conf.urls import url

from .views import view_category, view_post

urlpatterns = [
            url(r'^(?P<post_name>[\w-]+)/$', view_post, name='view_post'),
              ]
