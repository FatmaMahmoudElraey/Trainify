from django import forms
from .models import Tracks

class TracksForm(forms.ModelForm):
    class Meta:
        model = Tracks
        # fields = '__all__'
        fields = ['name', 'hours', 'picture']