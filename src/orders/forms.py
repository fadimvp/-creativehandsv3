from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'phone', 'address_1', 'address_2', 'country', 'state', 'city',
                  'order_note', 'i_agree', ]

    def clean(self):
        cleaned_data = self.cleaned_data
        i_agree = cleaned_data.get('i_agree')
        if i_agree == False:
            raise forms.ValidationError("plase ckeck  true ")
