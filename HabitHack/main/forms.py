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

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',  'password1', 'password2', 'email',
        ]
        widgets = {
            'username' : forms.TextInput(attrs={'placeholder' : 'Username'}),
            'password1' : forms.PasswordInput(attrs={'placeholder' : 'Password'}),
            'password2' : forms.PasswordInput(attrs={'placeholder' : 'ConfirmPassword'}),
            'email' : forms.EmailInput(attrs={'placeholder' : 'Email'})
        }

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2', 'email']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].label = ""

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            # 'first_name', 'last_name', 'email', 
            'birth_date',
            'gender', 'city', 'country', 'profile_photo',
        ]

