
from django import forms
from Userapp.models import UserProfile

class SignupForm(forms.ModelForm):
    user = forms.CharField(max_length=150, required=True,)
    email = forms.EmailField(max_length=50)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = UserProfile
        fields = ('user', 'first_name', 'last_name','email','password')


class SigninForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())