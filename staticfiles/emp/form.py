from django import forms

class contect(forms.Form):
    name=forms.CharField(max_length=200)
    email=forms.EmailField()
    content=forms.Textarea()