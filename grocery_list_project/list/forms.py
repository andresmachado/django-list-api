from django import forms
from django.forms import inlineformset_factory

from .models import List, Product


ListFormSet = inlineformset_factory(
    List,
    Product,
    fields=('name', 'quantity', 'price'),
    can_delete=False,
    extra=1,
)


class CreateListForm(forms.ModelForm):

    class Meta:
        """Settings for CreateListForm."""

        model = List
        fields = ('name', )
