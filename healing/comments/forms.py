from django import forms
from comments.models import Comments
from django.forms import ModelForm, Textarea


class CommentsForm(ModelForm):

    class Meta:
        model = Comments
        fields = ('text',)
        widgets = {
            'text': Textarea(attrs={'cols': 40, 'rows': 15}),
        }
