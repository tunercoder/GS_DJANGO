from cProfile import label
from socket import fromshare
from tkinter import Widget
from django import forms
from .models import User


class UserRegisterationForm(forms.ModelForm):
    name = forms.CharField(max_length=50, required=False)#extra validation on form field
    class Meta:
        model = User
        fields=['name','email','password']
        labels={'name':'Enter Name','email':'Enter Email id','password':'Enter Password'}
        help_text={'name':'full name here'}
        # error_messages={'name':{'required':'this field is required must be given'},
        # 'password':{'required':'password dal lo bhai jarurui hai'}}

        widgets={'password':forms.PasswordInput(attrs={'class':'passwordclass','placeholder':'strong password here!'})}

    