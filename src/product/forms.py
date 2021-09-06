from  django import forms

class SearchForm(forms.Form):
    query = forms.CharField(max_length=50)
    catid = forms.IntegerField()


class ReviewForm (forms.ModelForm):
    class Meta:
            fields =['subject','review','rating',]