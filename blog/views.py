from django.shortcuts import render
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Memories
from .forms import MemoryForm


def index(request):
    """ A view to return the index page """
    return render(request, 'index.html')


class Memorieslist(LoginRequiredMixin, generic.ListView):
    model = Memories
    queryset = Memories.objects.order_by("-created_on")
    template_name = "memories.html"
    paginate_by = 12


class MemoryPost(LoginRequiredMixin, View):
    def get(self, request):
        context = {'form': MemoryForm()}
        return render(request, 'memory_form.html', context)
