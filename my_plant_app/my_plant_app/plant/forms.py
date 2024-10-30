from django import forms
from my_plant_app.plant.models import Plant


class PlantBaseForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'


class PlantCreateForm(PlantBaseForm):
    pass


class PlantEditForm(PlantBaseForm):
    pass


class PlantDeleteForm(PlantBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['plant_type'].widget.attrs['disabled'] = True

        for field_name in self.fields:
            if field_name in self.fields:
                self.fields[field_name].widget.attrs['readonly'] = True
