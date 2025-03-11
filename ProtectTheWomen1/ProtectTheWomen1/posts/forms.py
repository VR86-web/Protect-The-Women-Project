from django import forms
from ProtectTheWomen1.posts.models import Post, Comment


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user',)
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Enter post title',
            }),
            'content': forms.Textarea(attrs={
                'placeholder': 'Write your post content here...',
                'rows': 5
            }),
        }
        labels = {
            'title': 'Post Title',
            'content': 'Post Content',
        }
        error_messages = {
            'title': {
                'required': 'Title cannot be empty.',
                'max_length': 'Title is too long.',
            },
            'content': {
                'required': 'Content is required to create a post.',
            },
        }


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

