from django import forms
from django.core import validators

def starts_with_s(value):
	if value[0] == 'p':
		raise forms.ValidationError('Name should start with p')


class StudentregistrationForm(forms.Form):
    stuid = forms.IntegerField()
    name = forms.CharField(min_length=5,help_text='enter your name here',initial='Ashish',validators=[validators.MaxLengthValidator(10)])
    email = forms.EmailField(label='Email ID',disabled=False,validators=[starts_with_s])
    password = forms.CharField(widget=forms.PasswordInput(attrs={'initial':'password dalo'}))
    comment = forms.CharField(widget=forms.Textarea(attrs={'class':'somecss1 somecss2', 'id':'uniqueid'}))


    def clean_name(self):
        valname = self.cleaned_data['name']
        if valname[0:1] == 'S' :
            raise forms.ValidationError('name should not start with s character')
        print('############22',valname)
        return valname
        

    # #clean method for whole form with more than one related fields ///Validation of Complete Django Form at once
    def clean(self):
        cleaned_data = super().clean()
        print('############33',cleaned_data)
        valname = self.cleaned_data.get('name','')
        valcomment = self.cleaned_data['comment']
        if valname[0:2] == 'NI' or len(valcomment) < 2:
            raise forms.ValidationError('start name char cannot be NI or comment len < 2 ')
        