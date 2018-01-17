from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import View
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods

from .models import UserHabit, HabitHistory



@login_required
def home(request):
    user_habits = UserHabit.objects.filter(user=request.user)

    habits = []

    for habit in user_habits:
        habit_records = HabitHistory.objects.filter(user_habit=habit)
        records = {}
        for rec in habit_records:
            records[rec.datehash] = rec.counter

        habits.append({ 
            'id': habit.id,
            'name': habit.name,
            'weekdays': habit.weekdays,
            'num_repeats': habit.num_repeats,
            'history': records
        })
    
    print(habits)

    return render(request, 'main/home.html', { 'habits': habits })
