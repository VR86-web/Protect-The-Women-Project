from django import forms

from ProtectTheWomen.common.models import Comments


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('content',)

        error_messages = {
            'content': {
                'required': 'Please enter your comment.',
            },
        }





