from django import forms
from fruitpedia.fruit.models import Fruit
from mixins import RemoveLabelMixin


class FruitCreateForm(RemoveLabelMixin, forms.ModelForm):
    class Meta:
        model = Fruit
        exclude = ['owner']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Fruit Name'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'Fruit Image URL'}),
            'description': forms.Textarea(attrs={'placeholder': 'Fruit Description'}),
            'nutrition': forms.Textarea(attrs={'placeholder': 'Fruit Nutrition'})
        }
