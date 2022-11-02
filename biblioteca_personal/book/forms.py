from django import forms
from book.models import Book

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


class BookForm(forms.ModelForm):
    STATUSS = (
        ('Read', 'Read'),
        ('Reading', 'Reading'),
        ('No Read', 'No Read')
    )
    LIBREROS = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    RATINGS = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
    )

    
    title = forms.CharField(
        label='Title', 
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', })
        )
    price = forms.DecimalField(
        label='Price',
        required=True,
        decimal_places=2, 
        max_digits=6,
        widget=forms.TextInput(attrs={'class': 'form-control',})
        )
    status = forms.ChoiceField(
        label='Select status',
        widget=forms.RadioSelect(attrs={'class': 'form-check form-check-inline',}), 
        choices=STATUSS
        )
    librero = forms.ChoiceField(
        label = 'Library',
        required=False, 
        widget=forms.RadioSelect(attrs={'class': 'form-check form-check-inline',}), 
        choices=LIBREROS
        )
 
    rating = forms.ChoiceField(
        label = 'Rating',
        required=True, 
        widget=forms.RadioSelect(attrs={'class': 'form-check form-check-inline',}), 
        choices=RATINGS
        )
    comment = forms.CharField(
        label='Comment',
        required=False,  
        widget=forms.Textarea(attrs={'placeholder': 'Max 500 words.',
                                     'class': 'form-control'})
        )


    class Meta:
        model = Book
        fields =  [
            'title',
            'price',
            'status' ,
            'librero',
            'id_author',
            'id_category',
            'rating',
            'comment',
        ]

        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'title',
            'price',
            'status' ,
            'librero',
            'id_author',
            'id_category',
            'rating',
            'comment',  
        )
    