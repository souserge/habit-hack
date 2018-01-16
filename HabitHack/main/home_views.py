from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import View
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods


@login_required
def home(request):
    return render(request, 'main/home.html')
