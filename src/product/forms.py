from django import forms
from .models import ReviewRating
from localflavor import generic
from localflavor.generic.forms import BICFormField, IBANFormField

class MyForm(forms.Form):
    my_date_field = generic.forms.DateField()
    iban = IBANFormField()
    bic = BICFormField()
class SearchForm(forms.Form):
    query = forms.CharField(max_length=50)
    catid = forms.IntegerField()


class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewRating
        fields = ['subject', 'review', 'rating']
