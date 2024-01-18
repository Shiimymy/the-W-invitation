from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Memories
from .forms import MemoryForm


def index(request):
    """ A view to return the index page """
    return render(request, 'index.html')


class Memorieslist(LoginRequiredMixin, generic.ListView):
    """
    Renders the Memories page
    """
    model = Memories
    template_name = "memories.html"
    paginate_by = 9

    def get_queryset(self):

        """
        Filter Memories by location and/or inviter in the page
        """

        memories = Memories.objects.filter(approved=True).order_by("-created_on")
        selected_location = self.request.GET.get('location', '')
        selected_inviter = self.request.GET.get('inviter', '')        
        
        if selected_location:
            memories = memories.filter(location=selected_location)

        if selected_inviter:
            memories = memories.filter(inviter__contains=selected_inviter)

        return memories


class MemoryPost(LoginRequiredMixin, View):
    """
    A view to redirect to memory_form.html for login users
    and add a memory
    """
    def get(self, request):
        context = {'form': MemoryForm()}
        return render(request, 'memory_form.html', context)

    def post(self, request):
        memory_form = MemoryForm(request.POST, request.FILES)
        print(memory_form.errors)
        if memory_form.is_valid():
            memory = memory_form.save(commit=False)
            memory.author = request.user
            memory.image = memory_form.cleaned_data.get('image')
            memory.location = memory_form.cleaned_data.get('location')
            memory.inviter = memory_form.cleaned_data.get('inviter')
            memory.save()
            messages.add_message(request, messages.SUCCESS, "Memory submited, it will show once approved by admin.")
            return redirect('memories')
        else:
            context = {'form': memory_form}
            return render(request, 'memory_form.html', context)


@login_required
def edit_memory(request, memory_id):
    """Edit Memory if login"""
    memory = get_object_or_404(Memories, id=memory_id)

    if request.method == 'POST':
        memory_form = MemoryForm(request.POST, request.FILES, instance=memory)

        if memory_form.is_valid():
            memory = memory_form.save(commit=False)
            memory.approved = False
            memory.save()
            messages.add_message(request, messages.SUCCESS, "Memory updated, itwill show once approved by admin.")        
            return redirect('memories')
    else:
        memory_form = MemoryForm(instance=memory)

    context = {'form': memory_form}
    return render(request, 'edit.html', context)


@login_required
def delete_memory(request, memory_id):
    """Delete Memory if login"""
    memory = get_object_or_404(Memories, id=memory_id)
    memory.delete()
    messages.add_message(request, messages.WARNING, "Memory deleted successfuly!") 
    return redirect('memories')
