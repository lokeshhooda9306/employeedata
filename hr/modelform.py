from dataclasses import fields
from django import forms
from .models import hooda


class hoodareg(forms.ModelForm):
    class Meta:
        model = hooda
        fields = "__all__"