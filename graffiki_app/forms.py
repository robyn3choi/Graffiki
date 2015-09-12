from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.ImageField()
    image = forms.FileField(label='Select an image')


class ProfileImageForm(forms.Form):
    image = forms.FileField(label='Select a profile Image')