from django import forms

from ProtectTheWomen1.posts.models import Post, Comment


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"


class PostCreateForm(PostBaseForm):
    pass


class PostEditForm(PostBaseForm):
    pass


class PostDeleteForm(PostBaseForm):
    pass


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'content',)

        labels = {
            'author': '',
            'content': '',
        }

        error_messages = {
            'author': {
                'required': 'Author name is required. Write it!',
            },
            'content': {
                'required': 'Content is required. Write it!',
            },
        }

        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name:'}),

            'content': forms.Textarea(attrs={'class': 'form-control mb-3', 'placeholder': 'Write your comment...'}),

        }
