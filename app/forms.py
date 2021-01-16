from django import forms

from .models import Post


class PostUpload(forms.ModelForm):
    caption = forms.CharField(max_length=80)
    image = forms.ImageField()

    class Meta:
        model = Post
        fields = '__all__'
