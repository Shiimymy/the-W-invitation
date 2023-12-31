from django.urls import path
from . import views

"""url paths"""
urlpatterns = [
    path('', views.index, name='home'),
    path('memories/', views.Memorieslist.as_view(), name='memories'),
    path('memory_form/', views.MemoryPost.as_view(), name='memory_form'),
    path('edit/<int:memory_id>/', views.edit_memory, name='edit'),
    path('delete/<int:memory_id>/', views.delete_memory, name='delete'),
]
