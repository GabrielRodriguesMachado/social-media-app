from django import forms
from .models import Comment

from .models import Post

CLASS_INPUT = "w-full py-4 px-6 rounded-xl"


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("content",)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("content", "image")

    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "What's on your mind?",
                "class": CLASS_INPUT,
            }
        )
    )

    image = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                "class": CLASS_INPUT,
            }
        ),
        required=False,
    )
