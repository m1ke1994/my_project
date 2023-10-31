from django import forms
from .models import Order
from my_first_app.models import Аpartments

class OrderForm(forms.ModelForm):
    personal_data=forms.BooleanField(label="Я согласен на обработку персональных данных", required=True)

    class Meta:
        model = Order
        fields = ['apartment', 'name', 'phone']