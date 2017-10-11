from django import forms
from myApp.models import Player, UserProfileInfo
from django.contrib.auth.models import User


class NewPlayerForm(forms.ModelForm):
    class Meta():
        model = Player
        fields = "__all__"

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')
