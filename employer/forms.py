from django import forms
from django.contrib.auth.models import User
from .models import Request
#from django.contrib.auth.forms import UserCreationForm
#from django.forms import modelformset_factory

class RequestCreationForm(forms.ModelForm):
    
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