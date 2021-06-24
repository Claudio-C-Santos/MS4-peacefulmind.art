from django import forms

from .models import customOrder


class newCustomOrderForm(forms.ModelForm):

    class Meta:
        model = customOrder
        fields = '__all__'
