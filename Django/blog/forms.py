from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post


class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=254,
                            required=True,
                            help_text='',
                            label='Post title:',
                            initial='Title your post...',)
    text = forms.CharField(widget=forms.Textarea,
                           required=True, help_text='',
                           label='Post text:',
                           initial='Write anything you want here.')

    class Meta:
        model = Post
        fields = ('title', 'text',)


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30,
                                 required=False,
                                 help_text='Optional.')
    last_name = forms.CharField(max_length=30,
                                required=False,
                                help_text='Optional.')
    email = forms.EmailField(max_length=254,
                             help_text='Required.')

    class Meta:
        model = User
        fields = ('username',
                  'first_name',
                  'last_name',
                  'email',
                  'password1',
                  'password2',)
