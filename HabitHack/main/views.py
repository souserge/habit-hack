from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import View
from django.views import generic
from django.views.generic.base import TemplateView
from .forms import RegistrationForm

# Create your views here.
# def index(request):
#     """
#         The main view of our website
#     """

#     # Data can be passed to template via context dictionary
#     # The context consists of pairs of name (string) and value (any object)
#     # Templates can then refer to these names and retrieve the data
#     context = {
#         'a_string': 'this is a test of passing data to a template',
#         'a_number': 7357
#     }

#     return render(request, 'index.html', context)

class HomePage(TemplateView):
    template_name = 'main/index_test.html'

# User sign up view
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('main:index')
    else:
        form = RegistrationForm()
    return render(request, 'main/register_test.html', {'form': form})