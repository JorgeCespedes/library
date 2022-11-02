from unicodedata import category
from django import forms
from category.models import Category

# class CategoryForm(forms.Form):
#     category = forms.CharField(label='Category', max_length=100)
    


class CategoryForm(forms.ModelForm):
    
    category = forms.CharField(
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Category',
                                      'class':'form-control'}) 
        )
    
    class Meta:
        model = Category
        fields = '__all__'