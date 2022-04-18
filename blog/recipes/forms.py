from .models import *
from django import forms

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = ['title', 'img', 'description', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            # 'img': forms.FileInput(attrs={'class': 'form-control-file'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),

        }

class RecipeListForm(forms.ModelForm):
    class Meta:
        model= RecipeList
        fields = ['ingredient', 'quantity']
        widgets = {
            'ingredient': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
         }

RecipeListFormSet = forms.inlineformset_factory(Recipes, RecipeList, form=RecipeListForm, extra=1)