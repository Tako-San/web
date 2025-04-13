"""Models for the 'core' app."""
from django.db import models

class HistoricalEvent(models.Model):
    """Represents an historical event."""
    CATEGORY_CHOICES = [
        ('war', 'Войны'),
        ('discovery', 'Открытия'),
        ('culture', 'Культура'),
    ]
    date = models.DateField()
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='events/', blank=True, null=True)

class QuizQuestion(models.Model):
    """Represents a quiz question."""
    question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100, blank=True)
    option4 = models.CharField(max_length=100, blank=True)
    correct_answer = models.CharField(max_length=100)
