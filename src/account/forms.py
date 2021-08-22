from django import forms
from .models import Account


class RegistertionForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={

        'placeholder': 'Enter password here ',
        'class': 'form-control'
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={

        'placeholder': 'Enter confirm_password   ',
        'class': 'form-control'
    }))

    class Meta:
        model = Account
        fields = ['first_name', 'username', 'last_name', 'phone_number', 'email', 'password']

    def __init__(self, *args, **kwargs):
        super(RegistertionForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder '] = 'please  enter your email '

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def clean(self):

        cleaned_data = super(RegistertionForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("password not match ! ")
