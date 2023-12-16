from .models import Memories
from django import forms
from crispy_forms.helper import FormHelper


class MemoryForm(forms.ModelForm):

    class Meta:
        model = Memories
        fields = ('image', 'content', )
