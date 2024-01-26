from .models import Memories
from django import forms


class MemoryForm(forms.ModelForm):
    """
    Form for Memories
    """

    class Meta:
        model = Memories
        fields = ('image', 'location', 'inviter', 'content',)
        widgets = {'content': forms.Textarea(attrs={'maxlength': '200', })}
