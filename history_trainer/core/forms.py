from django import forms
from .models import HistoricalEvent, QuizQuestion

class EventForm(forms.ModelForm):
    class Meta:
        model = HistoricalEvent
        fields = ['date', 'description', 'category', 'image']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

class QuizForm(forms.ModelForm):
    class Meta:
        model = QuizQuestion
        fields = ['question', 'option1', 'option2', 'option3', 'option4', 'correct_answer']
