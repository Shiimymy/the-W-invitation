from django.urls import path
from . import views
from django.conf.urls import handler500, handler404
from .views import custom_500, custom_404

"""url paths"""
urlpatterns = [
    path('', views.index, name='home'),
    path('memories/', views.Memorieslist.as_view(), name='memories'),
    path('memory_form/', views.MemoryPost.as_view(), name='memory_form'),
    path('edit/<int:memory_id>/', views.edit_memory, name='edit'),
    path('delete/<int:memory_id>/', views.delete_memory, name='delete'),
]


handler500 = 'blog.views.custom_500'
handler404 = 'blog.views.custom_404'