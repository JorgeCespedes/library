from django import forms
from author.models import Author


class AuthorForm(forms.ModelForm):
    
    full_name = forms.CharField(
        label='', 
        widget=forms.TextInput(attrs={'placeholder': 'Name',
                                      'class': 'form-control',}) )
    
    class Meta:
        model = Author
        fields = [
            "full_name",
        ]