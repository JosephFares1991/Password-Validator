from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core import validators
from english_words import get_english_words_set
from django.core.exceptions import ValidationError



web2lowerset = get_english_words_set(['web2'], lower=True)

def dictionaryValidation(password):
    for i in range(0, len(password)+1):
        start = i
        for j in range(i+2, len(password)+1):
            sub_password = password[start:j]
            if(sub_password in web2lowerset):                
               return True

def maximumCharacters(password):
    if len(password) > 16:
        return True


class MyUserCreationForm(UserCreationForm):    
    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2')

    def clean_password1(self):
        password = self.cleaned_data['password1']
        # Do whatever you want
        if dictionaryValidation(password=password):
            raise forms.ValidationError("Password constains common English Word")
        
        if maximumCharacters(password=password):
             raise forms.ValidationError("Password length exceeds 16 character")        


class LoginForm(forms.Form):
    username = forms.CharField() 
    password = forms.CharField(widget=forms.PasswordInput())
   