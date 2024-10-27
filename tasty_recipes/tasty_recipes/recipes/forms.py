from django import forms
from tasty_recipes.recipes.models import Recipe


class RecipeBaseForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ['author']

        widgets = {
            'ingredients': forms.Textarea(attrs={'placeholder': "ingredient1, ingredient2, ..."}),
            'instructions': forms.Textarea(attrs={'placeholder': "Enter detailed instructions here..."}),
            'image_url': forms.URLInput(attrs={'placeholder': "Optional image URL here..."})
        }


class RecipeCreateForm(RecipeBaseForm):
    pass



class RecipeUpdateForm(RecipeBaseForm):
    pass


class RecipeDeleteForm(RecipeBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['cuisine_type'].widget.attrs['disabled'] = True

        for field_name in self.fields:
            if field_name in self.fields:
                self.fields[field_name].widget.attrs['readonly'] = True
