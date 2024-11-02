from django import forms
from furry_funnies.post.models import Post


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['updated_at', 'author']


class PostCreateForm(PostBaseForm):
    class Meta(PostBaseForm.Meta):

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': "Put an attractive and unique title..." }),
            'content': forms.Textarea(attrs={'placeholder': "Share some interesting facts about your adorable pets..."})
        }


class PostEditForm(PostBaseForm):
    class Meta(PostBaseForm.Meta):

        help_texts = {
            'image_url': ''
        }


class PostDeleteForm(PostBaseForm):
    class Meta(PostEditForm.Meta):
        pass

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name in self.fields.values():
                field_name.widget.attrs['readonly'] = 'readonly'