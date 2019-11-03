from django.contrib.auth.models import User
from django import forms
from .models import Assignment, Course, FileSubmit
from django.contrib.admin.widgets import AdminDateWidget

class HWForm(forms.ModelForm):
    expiration_date = forms.DateField(widget=forms.SelectDateWidget)
    class Meta:
        model = Assignment
        # fields = ('class_choice','class_div', 'expiration_date', 'title', 'body')
        fields = '__all__'


class FileForm(forms.ModelForm):
    class Meta:
        model = FileSubmit
        fields = ('assignment','title', 'myfile', 'body')

        # fields = '__all__'
