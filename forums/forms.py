from django import forms
from .models import Post

class TopicCreateForm(forms.Form):
    topic = forms.CharField(label="Topic", min_length=3)
    message = forms.CharField(label="Message", min_length=3, widget=forms.Textarea())
    # image = forms.FileField(label="image")

class PostCreateForm(forms.Form):
    message = forms.CharField(label="Message", min_length=3, widget=forms.Textarea())
    image = forms.FileField(label="image")
# class UploadFileForm(forms.Form):
#     title = forms.CharField(max_length=50)
#     file = forms.FileField()

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file'
    )
