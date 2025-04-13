from django.shortcuts import render, redirect
from .models import HistoricalEvent, QuizQuestion
from .forms import EventForm, QuizForm

def home(request):
    return render(request, 'core/home.html')

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('events_table')
    else:
        form = EventForm()
    return render(request, 'core/add_event.html', {'form': form})

def events_table(request):
    category = request.GET.get('category', '')
    events = HistoricalEvent.objects.all()
    if category:
        events = events.filter(category=category)
    return render(request, 'core/events_table.html', {'events': events})

def take_quiz(request):
    questions = QuizQuestion.objects.all()
    return render(request, 'core/quiz.html', {'questions': questions})

def quiz_result(request):
    if request.method == 'POST':
        score = 0
        total = QuizQuestion.objects.count()
        for question in QuizQuestion.objects.all():
            user_answer = request.POST.get(f'question_{question.id}')
            if user_answer == question.correct_answer:
                score += 1
        return render(request, 'core/quiz_result.html', {'score': score, 'total': total})
    return redirect('quiz')
