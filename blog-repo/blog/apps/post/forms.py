#input para busqueda
#select por orden de mas relevantes, mas antiguos, mas recientes

from django import forms

class PostFilterForm(forms.Form):
    search_query = forms.CharField(
        required=False, 
        widget=forms.TextInput(
            attrs={'placeholder': 'Buscar...', 'class': 'w-full p-2 '}
        )
    )
    order_by=forms.ChoiceField(
        required=False,
        choices = (('-created_at', 'Mas recientes'),
        ('created_at', 'Mas antiguos'),
        ('-comments_count', 'Mas comentados'),
        ),
        widget=forms.Select(
            attrs={'class': 'w-full p-2'}
        )
    )