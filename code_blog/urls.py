from django.conf import settings
from django.contrib import admin
from django.conf.urls import include, url
from django.conf.urls.static import static

from django.conf.urls import (
    handler400, handler403, handler404, handler500
)
handler400 = 'blog.views.handler400'
handler403 = 'blog.views.handler403'
handler404 = 'blog.views.handler404'
handler500 = 'blog.views.handler500'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^', include('blog.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
