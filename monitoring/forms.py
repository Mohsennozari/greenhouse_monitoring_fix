from django import forms
from .models import GreenhouseData

class GreenhouseDataForm(forms.ModelForm):
    class Meta:
        model = GreenhouseData
        fields = ['temperature', 'humidity', 'light']
        labels = {
            'temperature': 'دما (سانتی‌گراد)',
            'humidity': 'رطوبت (درصد)',
            'light': 'نور (لوکس)',
        }