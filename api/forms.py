from django import forms
from .models import User
from django.core.exceptions import ValidationError

class RegistartionForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['email','password']
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email ya existe.")
        return email
    
