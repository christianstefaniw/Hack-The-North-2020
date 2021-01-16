from django import forms

from .models import Post, User


class PostUpload(forms.ModelForm):
    caption = forms.CharField(max_length=80)
    image = forms.ImageField()

    class Meta:
        model = Post
        fields = ('caption', 'image')


class Login(forms.ModelForm):
    name = forms.CharField(max_length=80, widget=forms.TextInput(attrs={'placeholder': 'Name'}))

    class Meta:
        model = User
        fields = '__all__'
