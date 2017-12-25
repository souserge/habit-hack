from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import View
from django.views import generic
from django.views.generic.base import TemplateView
from .forms import RegistrationForm, ProfileEditForm, LoginForm, UserEditForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods
from django.views.generic import FormView

# DO NOT DELETE! STILL TESTING()
# def index(request):
#     if request.user.is_authenticated:
#         return redirect('main:home')
#     else:
#         login_form = LoginForm()
#         register_form = RegistrationForm()
#         return render(request, 'main/index.html', {'login_form' : login_form, 'register_form' : register_form}) 

class MainView(TemplateView):
    template_name = 'main/index.html'

    def get(self, request, *args, **kwargs):
        login_form = LoginForm(self.request.GET or None)
        register_form = RegistrationForm(self.request.GET or None)
        context = self.get_context_data(**kwargs)
        context['login_form'] = login_form
        context['register_form'] = register_form
        return self.render_to_response(context)

# DO NOT DELETE! STILL TESTING()
# @require_http_methods(["POST"])
# def register(request):
#     form = RegistrationForm(request.POST)
#     if form.is_valid():
#         form.save()
#         username = form.cleaned_data.get('username')
#         raw_password = form.cleaned_data.get('password1')
#         user = authenticate(username=username, password=raw_password)
#         login(request, user)
#         return redirect('main:index')

# DO NOT DELETE! STILL TESTING()
# @require_http_methods(["POST"])
# def user_login(request):
#     form = LoginForm(data=request.POST)
#     if form.is_valid():
#         username = form.cleaned_data.get('username')
#         raw_password = form.cleaned_data.get('password')
#         user = authenticate(username=username, password=raw_password)
#         login(request, user)
#         return redirect('main:index')
#     else:
#         return HttpResponse("Error in logging in")

class RegistrationFormView(FormView):
    form_class = RegistrationForm
    template_name = 'main/index.html'
    #success_url = 'main/home.html'

    def get(self, request, *args, **kwargs):
        register_form = self.form_class()
        login_form = LoginForm()
        return self.render_to_response(
            self.get_context_data(
                login_form=login_form,
                register_form=register_form,
            )
        )


    def post(self, request, *args, **kwargs):
        register_form = self.form_class(request.POST)
        login_form = LoginForm()
        if register_form.is_valid():
            register_form.save()
            #return self.render_to_response(
                #self.get_context_data(
                #success=True
            #)
        #)
            username = register_form.cleaned_data.get('username')
            raw_password = register_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('main:home')
        else:
            return self.render_to_response(
            self.get_context_data(
                login_form=login_form,
                register_form=register_form,
            )
        )


class LoginFormView(FormView):
    form_class = LoginForm
    template_name = 'main/index.html'
    #success_url = 'main/home.html'

    def get(self, request, *args, **kwargs):
        login_form = self.form_class()
        register_form = RegistrationForm()
        return self.render_to_response(
            self.get_context_data(
                login_form=login_form,
                register_form=register_form,
            )
        )

    def post(self, request, *args, **kwargs):
        login_form = self.form_class(data=request.POST)
        register_form = RegistrationForm()
        if login_form.is_valid():
            #return self.render_to_response(
            #    self.get_context_data(
            #    success=True
            #)
        #)
            username = login_form.cleaned_data.get('username')
            raw_password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('main:home')
        else:
            return self.render_to_response(
            self.get_context_data(
                    login_form=login_form,
                    register_form=register_form
            )
        )


@login_required
def user_profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'main/profile.html', {'user': user, 'profile': user.profile})

# DO NOT DELETE! STILL TESTING()
# @login_required
# def edit_user_profile(request):
#     if request.method == 'POST':
#         form = ProfileEditForm(request.POST, request.FILES, instance=request.user.profile)

#         if form.is_valid():
#             form.save(commit=True)
#             return redirect('main:user', username=request.user.username)
#         else:
#             return render(request, 'main/edit_profile.html', {'form': form})
#     else:
#         form = ProfileEditForm(instance=request.user.profile)
#         return render(request, 'main/edit_profile.html', {'form':form})
        
@login_required
def edit_user_profile(request):
    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=request.user)
        user_profile_form = ProfileEditForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and user_profile_form.is_valid():
            user_form.save(commit=True)
            user_profile_form.save(commit=True)
            return redirect('main:user', username=request.user.username)
        else:
            return render(request, 'main/edit_profile.html', {'user_form': user_form, 
    'user_profile_form' : user_profile_form})
    else:
        user_form = UserEditForm(instance=request.user)
        user_profile_form = ProfileEditForm(instance=request.user.profile)
        return render(request, 'main/edit_profile.html', {'user_form': user_form,
    'user_profile_form' : user_profile_form})



@login_required
def home(request):
    return render(request, 'main/home.html')



