from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Profile


class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)


    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class ProfileUpdateForrm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

