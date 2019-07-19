from django import forms
from . import models 

class Post_Form(forms.ModelForm):
    """ form for the post model """

    class Meta():
        model = models.Post
        fields = ('author','title','text')

    widget = {
        'title':forms.TextInput(attrs={'class':'textinputclass'}),
        'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
    }

class Comment_Form(forms.ModelForm):
    """ form for the comment model """

    class Meta():
        model = models.Comment
        fields = ('author','text')

        widget = {
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }