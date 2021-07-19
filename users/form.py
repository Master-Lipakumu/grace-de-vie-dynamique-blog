from django.contrib.auth.models import User, auth

from django.contrib.auth.forms import UserCreationForm

from django import forms

from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    nom = forms.CharField(max_length = 100)
    prenom = forms.CharField(max_length = 100)

    class Meta():
        model = User
        fields = ['nom','prenom','email','username','password1','password2']


##################login form##############################
class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)
    class Meta():
        fields =['username','password']

#mise a jour des donnée

class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()
    class Meta():
        model = User
        fields = ['email','username']


# mise a jour du profile

class ProfileUpdateForm(forms.ModelForm):
    class Meta():
        model = Profile
        fields = ['image']