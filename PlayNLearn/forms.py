from django.forms import forms
from PlayNLearn.models import  User


class signUpForm(forms.Form):
    class Meta:
        model = User
        fields = ('email', 'uname', 'password',)