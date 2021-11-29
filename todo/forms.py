from django import forms
from .models import Item


# inherits functionality of ModelForm


class ItemForm(forms.ModelForm):
    # inner class gives ItemForm info about itself
    class Meta:
        model = Item
        fields = ['name', 'done']
