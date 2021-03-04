from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    # Meta class tells django which model we will use for our form. We have imported the Post model above
    class Meta:
        model = Post
        fields = ('title', 'text',)