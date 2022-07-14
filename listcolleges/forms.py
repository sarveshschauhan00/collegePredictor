from django import forms
from .models import RankTable

class RankForm(forms.ModelForm):
    class Meta:
        model = RankTable
        fields = ('gender', 'percentile', 'catagory', 'main_catagory_rank', 'advanced_general_rank', 'advanced_catagory_rank')

        widgets = {
            'gender':forms.Select(attrs={'class':'form-control'}),
            'percentile':forms.NumberInput(attrs={'class':'form-control'}),
            'catagory':forms.Select(attrs={'class':'form-control'}),
            'main_catagory_rank':forms.NumberInput(attrs={'class':'form-control'}),
            'advanced_general_rank': forms.NumberInput(attrs={'class': 'form-control'}),
            'advanced_catagory_rank': forms.NumberInput(attrs={'class': 'form-control'})
        }