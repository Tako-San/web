"""views.py"""

from django.shortcuts import render, redirect
from .models import HistoricalEvent, QuizQuestion
from .forms import EventForm  # QuizForm импортируется, но не используется

def home(request):
    """View function for the home page."""
    return render(request, 'core/home.html')

def add_event(request):
    """View function for adding a new historical event."""
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('events_table')
    else:
        form = EventForm()
    return render(request, 'core/add_event.html', {'form': form})

def events_table(request):
    """View function for displaying the table of historical events."""
    category = request.GET.get('category', '')
    events = HistoricalEvent.objects.all().order_by('date')  # pylint: disable=no-member
    if category:
        events = events.filter(category=category)
    return render(request, 'core/events_table.html', {'events': events})

def take_quiz(request):
    """View function for taking the quiz."""
    questions = QuizQuestion.objects.all()  # pylint: disable=no-member
    return render(request, 'core/quiz.html', {'questions': questions})

def quiz_result(request):
    """View function for displaying the quiz result."""
    if request.method == 'POST':
        score = 0
        total = QuizQuestion.objects.count()  # pylint: disable=no-member
        for question in QuizQuestion.objects.all():  # pylint: disable=no-member
            user_answer = request.POST.get(f'question_{question.id}')
            if user_answer == question.correct_answer:
                score += 1
        return render(request, 'core/quiz_result.html', {'score': score, 'total': total})  # pylint: disable=no-member
    return redirect('quiz')
