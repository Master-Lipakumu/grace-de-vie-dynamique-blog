from django import forms
from django.forms import ModelForm

from .models import Ncontacte


class Nscontacte(ModelForm):
    class Meta():
        model = Ncontacte
        fields = ['nom','prenom','email','sujet','messages']