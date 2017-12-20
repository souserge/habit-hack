from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import UserProfile

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',  'password1', 'password2', 'email',
        ]
        widgets = {
            'username' : forms.TextInput(attrs={'placeholder' : 'Username'}),
            #'password1' : forms.PasswordInput(attrs={'placeholder' : 'Password'}),
            #'password2' : forms.PasswordInput(attrs={'placeholder' : 'ConfirmPassword'}),
            'email' : forms.EmailInput(attrs={'placeholder' : 'Email'})
        }

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2', 'email']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].label = ""
        self.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder': 'Password'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder': 'Confirm Password'})

class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = [
            'username',  'password'
        ]

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].label = ""
        self.fields['password'].widget = forms.PasswordInput(attrs={'placeholder': 'Password'})
        self.fields['username'].widget = forms.TextInput(attrs={'placeholder': 'Username'})


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            # these ones should be added
            # 'first_name', 'last_name', 

            'city', 'country', 'description', 'profile_photo',
            
            # these ones we don't actually need
            # 'birth_date','gender',
            
            # and these should be availible as well
            # 'password', 'confirm_password', 'email', 'confirm_email',
        ]

    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args, **kwargs)

        for fieldname in ['city', 'country', 'description', 'profile_photo']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].label = ""
        self.fields['city'].widget = forms.TextInput(attrs={'placeholder': 'City'})
        self.fields['country'].widget = forms.TextInput(attrs={'placeholder': 'Country'})
        self.fields['description'].widget = forms.Textarea(attrs={'placeholder' : 'Write about yourself'})

