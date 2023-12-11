from .models import Memories
from django import forms


class MemoryForm(forms.ModelForm):
    image = forms.ImageField()
    content = forms.TextInput()

    class Meta:
        model = Memories
        fields = ('image', 'content', )
        
