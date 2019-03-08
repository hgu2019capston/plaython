from django.forms import ModelForm
from django import forms
from .models import Applicant
import subprocess
import re

class PostForm(ModelForm):

    OK = ((True, 'OK'),)
    aggrement = forms.BooleanField(widget=forms.RadioSelect(choices=OK))

    class Meta:
        model = Applicant
        fields = ['name','student_number','email','phone_number','usage','username','agreement']

    def clean_username(self):
        username = self.cleaned_data['username']
        special_case = re.findall("[^a-zA-Z0-9]", username)

        if special_case:
            raise forms.ValidationError("Do not use special characters(@,#,$,%)")

        if Applicant.objects.filter(username=username).exists():
            raise forms.ValidationError("The username is already in use")

        if subprocess.call(['grep', username, '/etc/passwd']) == 0:
            raise forms.ValidationError("The username is already in use")

        return username

