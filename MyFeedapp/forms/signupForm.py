from django import forms

class signUpForm(forms.Form):
    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput,
    )
    last_name= forms.CharField(
        required=True,
        widget=forms.TextInput,
    )
    username = forms.CharField(
        required=True,
        widget=forms.EmailInput,
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput
    )

class loginForm(forms.Form):
    username = forms.CharField(
        required=True,
        widget=forms.TextInput,
    )
    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput
    )
