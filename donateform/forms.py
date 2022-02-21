from django import forms

from donateform.models import Donateform

class donatesForm(forms.ModelForm):
  class Meta:
    model = Donateform

    fields = ("__all__")