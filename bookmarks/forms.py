from django import forms
from .models import Bookmark

class BookmarkForm(forms.ModelForm):
    class Meta:
        model = Bookmark
        fields = ['title', 'url', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

