from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SignUpForm(UserCreationForm):

    email = forms.EmailField(max_length=200, help_text='Required valid email address')

    class Meta:
        model = User
        fields = ('username','email','password1','password2')

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


class SelectRoleForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['role']
