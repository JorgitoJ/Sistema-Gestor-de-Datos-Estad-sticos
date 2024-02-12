from dataclasses import field
from pyexpat import model
from django import forms

from app.models import HojaCargo, InformePCR



class HojaCargoForm(forms.ModelForm):
    class Meta:
        model = HojaCargo
        fields = '__all__'
        exclude = ['fecha']

class InformePCRForm(forms.ModelForm):

    class Meta :
        model = InformePCR
        fields = '__all__'
        exclude = ['fecha']