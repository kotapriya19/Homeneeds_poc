from django import forms
from .models import Expense
import datetime

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['category', 'description', 'quantity', 'amount', 'date']
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class MonthYearForm(forms.Form):
    month = forms.IntegerField(
        min_value=1, max_value=12,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Month (1-12)'})
    )
    year = forms.IntegerField(
        min_value=2000, max_value=datetime.date.today().year,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Year'})
    )
