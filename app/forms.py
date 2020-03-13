"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class NewAccountForm(forms.Form):

    username=forms.CharField(max_length=254,
                             widget=forms.TextInput({
                                 'class':'form-control',
                                 'placeholder':'User Name',
                                 'required':''}))
    email=forms.CharField(max_length=254,
                             widget=forms.EmailInput({
                                 'class':'form-control',                                 
                                 'placeholder':'Email',
                                 'required':''}))
    
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password',
                                   'required':''}))

    passwordconfirmation = forms.CharField(label=_("Password confirmation"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password',
                                   'required':''}))

    



