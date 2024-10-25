from django import forms
from world_of_speed.car.models import Car


class CarBaseForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ['owner']

        widgets = {
            'image_url': forms.URLInput(attrs={'placeholder': "https://..."})
        }


class CarCreateForm(CarBaseForm):
    pass


class CarUpdateForm(CarBaseForm):
    pass


class CarDeleteForm(CarBaseForm):
    pass
