from django import forms

from .models import Candy


class CandyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CandyForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
    class Meta:
        model = Candy
        exclude = ['supplier']