from django import forms

from .models import List


class ListCreate(forms.ModelForm):

    class Meta:
        model = List
        fields = ('creator', 'name')
