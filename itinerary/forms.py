from django import forms
from .models import Itinerary

class ItineraryForm(forms.ModelForm):
    class Meta:
        model = Itinerary
        fields = ['source', 'destination', 'days', 'budget', 'travel_style']
        widgets = {
            'source': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your starting location'
            }),
            'destination': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Where do you want to go?'
            }),
            'days': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1,
                'max': 30,
                'placeholder': 'Number of days'
            }),
            'budget': forms.Select(attrs={'class': 'form-control'}),
            'travel_style': forms.Select(attrs={'class': 'form-control'}),
        }
