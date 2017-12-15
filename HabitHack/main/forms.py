from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from .models import UserProfile


# test form, delete it afterwards
class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

# User sign up form
# class RegistrationForm(UserCreationForm):
#     first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
#     last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
#     email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

#     class Meta:
#         model = User
#         fields = ('username', 'first_name', 'last_name', 
#         'email', 'password1', 'password2', )

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name', 
            'email', 'password1', 'password2',
        ]
    # first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    # last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    # email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')



class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            # 'first_name', 'last_name', 'email', 
            'birth_date',
            'gender', 'city', 'country', 'profile_photo',
        ]

    # first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    # last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    # email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    # birth_date = forms.DateField(required=False, help_text='Optional.')
    # gender = forms.ChoiceField(choices=(UserProfile.gender_choice))
    # city = forms.CharField(max_length=50, required=False, help_text='Optional.')
    # country = forms.CharField(max_length=50, required=False, help_text='Optional.')
    # profile_photo = forms.CharField(max_length=500, required=False, help_text='Optional.')

