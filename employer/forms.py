from django import forms
from django.contrib.auth.models import User
from .models import Request
from django_select2.forms import *
#from django.contrib.auth.forms import UserCreationForm
#from django.forms import modelformset_factory

class RequestCreationForm(forms.ModelForm):
    SKILL_CHOICES=[
        ('Java','Java'),
        ('C++','C++'),
        ('C','C'),
        ('Python','Python'),
        ('HTML','HTML'),
        ('CSS','CSS'),
        ('JS','Java Script'),
        ('PHP','PHP')
    ]
    skills=forms.MultipleChoiceField(choices=SKILL_CHOICES, widget=Select2MultipleWidget)
    class Meta:
        model = Request
        fields = [
            'skills',
            'experience',
            'notice_period',
            'location',
            'max_salary',
            'negotiable'
        ]