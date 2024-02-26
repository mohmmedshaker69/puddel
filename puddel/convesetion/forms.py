from django import forms

from .models import ConvesetionMessage

class ConvesetionMessageForm(forms.ModelForm):
    class Meta:
        model=ConvesetionMessage
        fields=('content',)
        widgets={
            'content': forms.Textarea(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            })
        }