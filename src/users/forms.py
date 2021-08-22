from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()


class Register_Form(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(
                                )
    password2 = forms.CharField(
                                )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username)
        if  qs.exists():
            raise forms.ValidationError("this is invalid user ")

        return username

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("this is email already used  ")

        return email


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", 'id': 'exampleInputPassword1'
                   }
        )
    )

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username)
        if not qs.exists():
            print(qs)
            print ("plase in")

            raise forms.ValidationError("this is invalid user ")

        return username
