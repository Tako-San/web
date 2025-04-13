from django.contrib import admin
from .models import HistoricalEvent, QuizQuestion

admin.site.register(HistoricalEvent)
admin.site.register(QuizQuestion)
