from django import forms
from .models import Lungs


class LungForm(forms.ModelForm):
    class Meta:
        model = Lungs
        fields = ('input_image',)
