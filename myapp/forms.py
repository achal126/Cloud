from django import forms
from myapp.models import Login
from django.shortcuts import render

class AuthenticationForm(forms.Form):
    username = forms.CharField(required= False)
    password = forms.CharField(required= False)

# class AuthenticationForm(forms.ModelForm):
#     Username = forms.CharField(widget=forms.widgets.TextInput, required= False)
#     Password = forms.CharField(widget=forms.widgets.PasswordInput, required=False)
#
#     class Meta:
#         model = Login
#         fields = ['Username', 'Password']
#
#     def clean_message(self):
#         username = self.cleaned_data.get("Username")
#         print username
#         dbuser = Login.objects.filter(email = username)
#
#         if not dbuser:
#             raise forms.ValidationError("User does not exist in our db!")
#         return username
