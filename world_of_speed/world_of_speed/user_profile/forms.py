from django import forms
from world_of_speed.user_profile.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

        widgets = {
            'password': forms.PasswordInput(),
        }

class ProfileCreateForm(ProfileBaseForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'age', 'password']


class ProfileUpdateForm(ProfileBaseForm):
    class Meta:
        model = Profile
        fields = '__all__'

        help_texts = {
            'age': ''
        }
