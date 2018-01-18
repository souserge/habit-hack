from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import View
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods

from .models import UserHabit, HabitHistory
from .forms import HabitEditForm


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
            record_counter = 0

            rec = None
            try:
                rec = HabitHistory.objects.filter(user_habit=habit).get(datehash=datehash)
                print("having " + str(rec.counter))
                record_counter = 1
                print("having " + str(record_counter))
                rec.counter += record_counter
                rec.save()
                print("saving " + str(record_counter))
            except HabitHistory.DoesNotExist:
                record_counter = 1
                rec = HabitHistory.objects.create(user_habit=habit, datehash=datehash, counter=record_counter)

            return HttpResponse(record_counter)


@login_required
def edit_habit(request, habit_id):
    habit = UserHabit.objects.get(id=habit_id)
    if request.method == 'POST':
        habit_form = HabitEditForm(request.POST, instance=habit)
        if habit_form.is_valid():
            habit_form.save();
            return redirect('main:home')
        else:
            return render(request, 'main/edit_habit.html', {'habit_form': habit_form})
    else:
        habit_form = HabitEditForm(instance=habit)      
        return render(request, 'main/edit_habit.html', {'habit_form': habit_form, 'habit_id': habit.id })


@login_required
def add_habit(request):
    if request.method == 'POST':
        habit_form = HabitEditForm(request.POST)
        if habit_form.is_valid():
            name = habit_form.cleaned_data.get('name')
            description = habit_form.cleaned_data.get('description')
            weekdays = habit_form.cleaned_data.get('weekdays')
            num_repeats = habit_form.cleaned_data.get('num_repeats')
            UserHabit.objects.create(user=request.user, name=name, description=description, weekdays=weekdays, num_repeats=num_repeats)

            return redirect('main:home')
        else:
            return render(request, 'main/add_habit.html', {'habit_form': habit_form})
    else:
        habit_form = HabitEditForm()      
        return render(request, 'main/add_habit.html', {'habit_form': habit_form })

@login_required
def delete_habit(request, habit_id):
    habit = UserHabit.objects.get(id=habit_id)
    habit.delete();
    return redirect('main:home')