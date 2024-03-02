from django import forms
from app1.models import Movie


class appform(forms.ModelForm):
    class Meta:
        model=Movie
        fields="__all__"