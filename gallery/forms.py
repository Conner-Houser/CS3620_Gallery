from django import forms
from .models import Comment

class ImageForm(forms.Form):
    user_image = forms.FileField()

class CommentForm(forms.ModelForm):
    class Meta: 
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={"rows": 3, "placeholder": "Add a comment..."})
        }