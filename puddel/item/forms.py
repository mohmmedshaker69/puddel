from django import forms

from .models import Item

INPUT_CLASSES='w-full py-4 px-6 rounde-xl border'

class NewitemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields=('category', 'name', 'description', 'price', 'image')

        widgets={
        'category':forms.Select(attrs={
            'class': INPUT_CLASSES
        }),
         'name':forms.TextInput(attrs={
            'class': INPUT_CLASSES
        }),
         'description':forms.Textarea(attrs={
            'class': INPUT_CLASSES
        }),
         'price':forms.TextInput(attrs={
            'class': INPUT_CLASSES
        }),
         'image':forms.FileInput(attrs={
            'class': INPUT_CLASSES
        })
    }
        

class EdititemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields=( 'name', 'description', 'price', 'image', 'is_sold')

        widgets={
       
         'name':forms.TextInput(attrs={
            'class': INPUT_CLASSES
        }),
         'description':forms.Textarea(attrs={
            'class': INPUT_CLASSES
        }),
         'price':forms.TextInput(attrs={
            'class': INPUT_CLASSES
        }),
         'image':forms.FileInput(attrs={
            'class': INPUT_CLASSES
        })
    }