from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import UserCostume


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = UserCostume
        fields = ('username', 'email', 'password1', 'password2',)




class LoginForm(forms.Form):
    username = forms.CharField(max_length=10)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
