from django import forms

class SearchForm(forms.Form):
    SearchText=forms.CharField(max_length=100,label="Fruit Name ",required=False)