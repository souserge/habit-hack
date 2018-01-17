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
    user = request.user
    user_habits = UserHabit.objects.filter(user_id=user.id)

    habits = []

    for habit in user_habits:
        habit_records = HabitHistory.objects.filter(user_habit_id=habit.id)
        records = {}
        for rec in habit_records:
            records.add(rec.datehash, rec.counter)

        habits.add({ 
            'id': habit.id,
            'name': habit.name,
            'weekdays': habit.weekdays,
            'num_repeats': habit.numRepeats,
            'history': records
        })

    return render(request, 'main/home.html', { 'habits': habits })
