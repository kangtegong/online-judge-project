from django.contrib.auth.models import User
from django import forms
from .models import MyUser

class RegisterForm(forms.ModelForm):
    username = forms.CharField(label='User ID', required=True)
    email = forms.EmailField(label='E-mail', required=True)
    realname = forms.CharField(label='Name', required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)
    
    class Meta:
        model = MyUser
        #fields = ('userid', 'username', 'email', 'phone', 'group')
        fields = ('username', 'email', 'group', 'realname')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords not matched!')
        return cd['password']