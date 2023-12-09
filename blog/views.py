from django.shortcuts import render, redirect
from django.views import generic, View
from .models import Memories


def index(request):
    """ A view to return the index page """
    return render(request, 'index.html')


class Memorieslist(generic.ListView):
    model = Memories
    queryset = Memories.objects.order_by("-created_on")
    template_name = "memories.html"
    paginate_by = 12


class MemoryPublication(generic.ListView):
    model = Memories
    template_name = "memory_form.html"
