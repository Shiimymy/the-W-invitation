from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls'), name='blog-urls'),
    path('accounts/', include('allauth.urls')),
    path('summernote/', include('django_summernote.urls')),
]
