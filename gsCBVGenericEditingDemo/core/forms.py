import email
from tkinter import Widget
from django import forms
from .models import Student

class ContactForm(forms.Form):
    name=forms.CharField( max_length=40)
    email=forms.EmailField()


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        widgets={'name':forms.TextInput(attrs={'class':'myclass'}),
        'password':forms.PasswordInput(attrs={'class':'myclass'})}
