from django import forms
from tasty_recipes.user_profile.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileCreateForm(ProfileBaseForm):
    class Meta:
        model = Profile
        exclude = ['bio']


class ProfileUpdateForm(ProfileBaseForm):
    pass


class ProfileDeleteForm(ProfileBaseForm):
    pass