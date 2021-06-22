from django import forms

from .models import communityCard


class newCardForm(forms.ModelForm):
    website = forms.URLField(initial='http://')

    class Meta:
        model = communityCard
        fields = '__all__'
