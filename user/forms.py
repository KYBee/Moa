from .models import Participant
from django import forms

from django.contrib.auth.forms import UserCreationForm

# Signup
class SignupForm(UserCreationForm):
    class Meta:
        model = Participant
        fields = ('email', 'username', 'password1', 'password2', 'is_agree')
        widgets = {
        }

# Login
class LoginForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ('email', 'password',)
        widgets = {
            'email': forms.TextInput(),
            'password': forms.PasswordInput(),
        }