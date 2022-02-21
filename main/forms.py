from django import forms

from main.models import Donor

class CustomerForm(forms.ModelForm):
  class Meta:
    model = Donor

    fields = ("__all__")