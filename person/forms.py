from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from person.choices import ProfileRoles


class SingUpForm(UserCreationForm):
    """ Class Form to User/Profile """
    rol = forms.ChoiceField(choices=ProfileRoles.CHOICES)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2', 'rol')

