from django.shortcuts import render, redirect, get_object_or_404
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
    
    def post(self, request):
        memory_form = MemoryForm(request.POST, request.FILES)
        if memory_form.is_valid():
            memory = memory_form.save(commit=False)
            memory.author = request.user
            memory.image = memory_form.cleaned_data.get('image')
            memory
            memory.save()
            return redirect('memories')
        else: 
            context = {'form': memory_form}
            return render(request, 'memory_form.html', context)

