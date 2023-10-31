from django import forms


class ApartamentsFilterForms(forms.Form):
    min_price=forms.IntegerField(label="от",required=False)
    max_price=forms.IntegerField(label="до",required=False)