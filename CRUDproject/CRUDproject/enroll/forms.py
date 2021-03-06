from django import forms
from django.db.models import fields
from django.forms import widgets 
from .models import student
from django.core import validators

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = student
        fields = ['name', 'email', 'password']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(render_value= True, attrs={'class':'form-control'}),
        }