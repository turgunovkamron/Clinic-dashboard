from django import forms

from app.models import User


class UserForms(forms.ModelForm):
    class Meta:
        model = User
        fields = 'name', 'familya','email','phone','info'
