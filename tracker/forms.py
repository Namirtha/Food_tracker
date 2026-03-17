from django import forms
from .models import FoodEntry, DailyGoal


class FoodEntryForm(forms.ModelForm):
    class Meta:
        model = FoodEntry
        fields = ['name', 'meal_type', 'calories', 'protein', 'carbs', 'fats', 'date']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Grilled Chicken Breast',
            }),
            'meal_type': forms.Select(attrs={'class': 'form-select'}),
            'calories': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'min': '0'}),
            'protein': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'min': '0'}),
            'carbs': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'min': '0'}),
            'fats': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.1', 'min': '0'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


class DailyGoalForm(forms.ModelForm):
    class Meta:
        model = DailyGoal
        fields = ['protein_goal', 'calorie_goal', 'carbs_goal', 'fats_goal']
        widgets = {
            'protein_goal': forms.NumberInput(attrs={'class': 'form-control', 'step': '1', 'min': '0'}),
            'calorie_goal': forms.NumberInput(attrs={'class': 'form-control', 'step': '1', 'min': '0'}),
            'carbs_goal': forms.NumberInput(attrs={'class': 'form-control', 'step': '1', 'min': '0'}),
            'fats_goal': forms.NumberInput(attrs={'class': 'form-control', 'step': '1', 'min': '0'}),
        }
