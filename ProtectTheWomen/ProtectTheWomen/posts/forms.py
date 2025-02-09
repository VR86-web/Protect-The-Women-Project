from django import forms

from ProtectTheWomen.posts.models import Posts
from ProtectTheWomen.posts.mixins import DisableFieldsMixin


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'content',]

        labels = {
            'title': 'Title',
            'content': 'Content',
        }


class PostsListForm(PostBaseForm):
    pass


class PostCreateForm(PostBaseForm):
    pass


class PostUpdateForm(PostBaseForm):
    pass


class PostDeleteForm(PostBaseForm, DisableFieldsMixin):
    disabled_fields = '__all__'


class SearchForm(forms.Form):
    query = forms.CharField(
        required=False,
        max_length=80,
    )



