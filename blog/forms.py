from .models import Memories
from django import forms
from crispy_forms.helper import FormHelper


class MemoryForm(forms.ModelForm):
    """
    Form for Memories
    """
    class Meta:
        model = Memories
        fields = ('image', 'content', )
