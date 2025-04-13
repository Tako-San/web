from django import forms
from .models import HistoricalEvent, QuizQuestion

class EventForm(forms.ModelForm):
    class Meta:
        model = HistoricalEvent
        fields = ['date', 'description', 'category', 'image']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    description = forms.CharField(
        max_length=500,  # Пример ограничения длины
        required=True,
        help_text="Введите описание события (максимум 500 символов)."
    )

    def clean_date(self):
        date = self.cleaned_data['date']
        #  Дополнительная валидация даты, если необходимо
        return date

class QuizForm(forms.ModelForm):
    class Meta:
        model = QuizQuestion
        fields = ['question', 'option1', 'option2', 'option3', 'option4', 'correct_answer']

    question = forms.CharField(
        max_length=200,
        required=True,
        help_text="Введите текст вопроса (максимум 200 символов)."
    )
    option1 = forms.CharField(
        max_length=100,
        required=True,
        help_text="Введите вариант ответа 1 (максимум 100 символов)."
    )
    option2 = forms.CharField(
        max_length=100,
        required=True,
        help_text="Введите вариант ответа 2 (максимум 100 символов)."
    )
    option3 = forms.CharField(
        max_length=100,
        help_text="Введите вариант ответа 3 (максимум 100 символов, необязательно)."
    )
    option4 = forms.CharField(
        max_length=100,
        help_text="Введите вариант ответа 4 (максимум 100 символов, необязательно)."
    )
    correct_answer = forms.CharField(
        max_length=100,
        required=True,
        help_text="Введите правильный ответ (максимум 100 символов)."
    )

    def clean(self):
        cleaned_data = super().clean()
        #  Дополнительная валидация формы, если необходимо
        return cleaned_data
