from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('memories/', views.Memorieslist.as_view(), name='memories'),
]
