from dataclasses import field
from django.core import validators
from django import forms
from .models import Book

class Reg(forms.ModelForm):
    class Meta:
        model=Book
        fields=['name','img','summary']
        widgets={
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'img': forms.TextInput(attrs={'class':'form-control'}),
            'summary': forms.TextInput(attrs={'class':'form-control'}),
        }