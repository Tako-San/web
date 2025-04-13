from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add-event/', views.add_event, name='add_event'),
    path('events/', views.events_table, name='events_table'),
    path('quiz/', views.take_quiz, name='quiz'),
    path('quiz-result/', views.quiz_result, name='quiz_result'),
]
