# forms.py
from django import forms
from .models import Institutions


class FormOne(forms.ModelForm):
    class Meta:
        model = Institutions
        fields = ['income', 'salary_payment', 'vehicle_procurement', 'construction']

    def save(self, commit=True):
        instance = super(FormOne, self).save(commit=False)

        # Calculate the sum and set it to the 'total' field
        instance.total = instance.salary_payment + instance.vehicle_procurement + instance.construction

        if commit:
            instance.save()

        return instance
