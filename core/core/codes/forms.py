from django import forms
from .models import VerificationCode


class CodeForm(forms.ModelForm):
    code = forms.CharField(label='Code', help_text='enter sms verification code')

    class Meta:
        model = VerificationCode
        fields = ('code',)
