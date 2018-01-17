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
        
    return render(request, 'main/home.html', { 'habits': habits })

@login_required
def increment_counter(request):
    habit_id = request.POST.get('habit_id', None)
    datehash = request.POST.get('datehash', None)
    print(habit_id + ', ' + datehash)
    if habit_id and datehash:
        habit = UserHabit.objects.get(id=int(habit_id))
        if habit.user == request.user:
            counter = 0

            rec = None
            try:
                rec = HabitHistory.objects.filter(user_habit=habit).get(datehash=datehash)
                coutner = rec.counter + 1
                rec.counter = counter
                rec.save()
            except HabitHistory.DoesNotExist:
                counter = 1
                rec = HabitHistory.objects.create(user_habit=habit, datehash=datehash, counter=counter)

            return HttpResponse(counter)
