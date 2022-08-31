from django.shortcuts import render
from django.http import HttpResponse
from .models import *

day_routine = {
    '8:00': 'Wake up', '8:10': 'brush your teeth', '8:30': 'have breakfast', '10:00': 'do some sports',
    '11:00': 'take a shower', '12:00 - 18:00': 'study', '18:00 - 19:00': 'break', '19:00 - 21:00': 'study',
    '21:00': 'supper', '23:00': 'go to sleep'
}


def greeting(request):
    return HttpResponse('Hello from Notes app.')


def routine(request):

    return render(request, 'notes/routine.html', {'day_routine': day_routine, 'title': 'My daily routine'})


def notes(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'title': 'Notes'
    }

    return render(request, 'notes/notes.html', context=context)
