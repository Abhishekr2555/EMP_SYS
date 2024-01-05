from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class signform(UserCreationForm):
    first_name=forms.CharField(max_length=15)
    last_name=forms.CharField(max_length=15)
    email=forms.CharField(max_length=20)

    class meta:
        model=User
        field=('username','password1','password2','email','first_name','last_name')

    def save(self,commit=True):
        user=super(signform.self).save(commit=False)
        user.email=self.cleaned_data['email']
        user.first_name=self.cleaned_data['first_name']
        user.last_name=self.cleaned_data['last_name']

        if commit:
            user.save()
        return user