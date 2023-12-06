from django.shortcuts import render
from django.views import generic
from .models import Memories


def index(request):
    """ A view to return the index page """
    return render(request, 'index.html')


class Memorieslist(generic.ListView):
    model = Memories
    queryset = Memories.objects.order_by("-created_on")
    template_name = "memories.html"
    paginate_by = 12