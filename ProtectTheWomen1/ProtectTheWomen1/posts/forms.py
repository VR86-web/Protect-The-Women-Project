from django import forms
from ProtectTheWomen1.posts.models import Post, Comment


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user',)


class PostCreateForm(PostBaseForm):
    pass


class PostEditForm(PostBaseForm):
    pass


class PostDeleteForm(PostBaseForm):
    pass


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)

        labels = {
            'content': '',
        }

        error_messages = {
            'content': {
                'required': 'Content is required. Write it!',
            },
        }

        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control mb-3', 'placeholder': 'Write your comment...'}),
        }

